import os
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        plaintext = file.read()
    ciphertext = fernet.encrypt(plaintext)
    with open(output_file, 'wb') as file:
        file.write(ciphertext)

input_file = 'example.txt'
output_file = 'example.txt.enc'
password = getpass.getpass("Enter encryption password: ").encode('utf-8')
salt = os.urandom(16)

key = generate_key(password, salt)

with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

with open("salt.bin", "wb") as salt_file:
    salt_file.write(salt)

encrypt_file(input_file, output_file, key)
os.remove(input_file)
