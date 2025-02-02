import os

# Server's address & port
SERVER_IP = "0.0.0.0"  # Ascultă pe toate interfețele de rețea
SERVER_PORT = 5001

# directory info
SAVE_DIRECTORY = "./uploads"
FILENAME_SIZE = 256

# data block size
CHUNK_SIZE = 4096  # 4KB

# AES Key
ENCRYPTION_KEY = b'Fortza_OtelulGL!'

# IV size
IV_LENGTH = 16

# Timeout
TIMEOUT = 30  # [sec]
