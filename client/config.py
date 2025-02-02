import os

# General configuration
SERVER_IP = "--"
SERVER_PORT = 5001
CHUNK_SIZE = 4096  # block of 4KB

# Security configuration
ENCRYPTION_KEY = b'Fortza_OtelulGL!'
IV_LENGTH = 16  # IV dimension for AES

FILENAME_SIZE = 256

# Other settings
RETRY_COUNT = 3  # no of retries
TIMEOUT = 10 
