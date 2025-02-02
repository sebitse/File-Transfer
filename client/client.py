import socket
import os
import hashlib
import struct
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import config

# Function to encrypt a block of data
def encrypt_data(data, cipher):
    return cipher.encrypt(data)

# Function to compute file hash
def compute_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(config.CHUNK_SIZE):
            hasher.update(chunk)
    return hasher.hexdigest()


def send_file(file_path, server_ip, server_port, gui_callback=None):
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    file_hash = compute_hash(file_path)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(config.TIMEOUT)

    try:
        client.connect((server_ip, server_port))
    except socket.timeout:
        error_msg = "⛔ Connection Failed: Timeout!"
        if gui_callback:
            gui_callback(error_msg)
        else:
            print(error_msg)
        return

    success_msg = f'🔄 Sending: {file_name} ({file_size} bytes)'
    if gui_callback:
        gui_callback(success_msg)
    else:
        print(success_msg)

    # Send metadata
    client.sendall(struct.pack('!Q', file_size))
    client.sendall(file_name.encode().ljust(config.FILENAME_SIZE, b'\0'))  # fixed length
    client.sendall(file_hash.encode())  

    # AES Initialization
    iv = get_random_bytes(config.IV_LENGTH)
    cipher = AES.new(config.ENCRYPTION_KEY, AES.MODE_CFB, iv)
    client.sendall(iv)  

    # Send file in chunks
    with open(file_path, 'rb') as f:
        while chunk := f.read(config.CHUNK_SIZE):
            encrypted_chunk = encrypt_data(chunk, cipher)
            client.sendall(encrypted_chunk)

    success_msg = '✅ Transfer completed!'
    if gui_callback:
        gui_callback(success_msg)
    else:
        print(success_msg)

    client.close()
