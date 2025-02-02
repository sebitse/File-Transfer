import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# AES Configuration
IV_LENGTH = 16  # AES IV size for CFB mode (16 bytes)
KEY_SIZE = 32   # AES-256 requires a 32-byte key

def generate_key():
    """Generate a secure AES encryption key."""
    return get_random_bytes(KEY_SIZE)

def encrypt_data(data: bytes, key: bytes, iv: bytes) -> bytes:
    """Encrypts a given data block using AES in CFB mode."""
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.encrypt(data)

def decrypt_data(encrypted_data: bytes, key: bytes, iv: bytes) -> bytes:
    """Decrypts a given encrypted data block using AES in CFB mode."""
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(encrypted_data)

def compute_hash(data: bytes) -> str:
    """Compute SHA-256 hash of the given data."""
    hasher = hashlib.sha256()
    hasher.update(data)
    return hasher.hexdigest()
