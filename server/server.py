import socket
import struct
import os
from Crypto.Cipher import AES
import hashlib
import config

def compute_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(config.CHUNK_SIZE):
            hasher.update(chunk)
    return hasher.hexdigest()

def decrypt_data(data, cipher):
    return cipher.decrypt(data)

def start_server(host, port, gui_callback=None):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    server_msg = f"📡 Server listening on {host}:{port}..."
    if gui_callback:
        gui_callback(server_msg)
    else:
        print(server_msg)

    while True:
        client, addr = server.accept()
        connection_msg = f"🔗 Connection established from {addr}"
        if gui_callback:
            gui_callback(connection_msg)
        else:
            print(connection_msg)

        # Receive metadata
        file_size = struct.unpack('!Q', client.recv(8))[0]
        file_name = client.recv(config.FILENAME_SIZE).decode().strip('\x00')
        file_hash = client.recv(64).decode()

        # AES Initialization
        iv = client.recv(config.IV_LENGTH)
        cipher = AES.new(config.ENCRYPTION_KEY, AES.MODE_CFB, iv)

        # Save received file
        save_path = os.path.join(config.SAVE_DIRECTORY, file_name)
        with open(save_path, 'wb') as f:
            received_bytes = 0
            while received_bytes < file_size:
                chunk = client.recv(config.CHUNK_SIZE)
                decrypted_chunk = decrypt_data(chunk, cipher)
                f.write(decrypted_chunk)
                received_bytes += len(chunk)

        # Verify Integrity
        received_hash = compute_hash(save_path)
        if received_hash == file_hash:
            success_msg = f"✅ File received successfully: {file_name}"
        else:
            success_msg = f"⚠️ Integrity check failed for {file_name}! File may be corrupted."

        if gui_callback:
            gui_callback(success_msg)
        else:
            print(success_msg)

        client.close()
