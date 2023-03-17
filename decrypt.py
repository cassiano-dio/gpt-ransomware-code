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

def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        ciphertext = file.read()
    plaintext = fernet.decrypt(ciphertext)
    with open(output_file, 'wb') as file:
        file.write(plaintext)

input_file = 'example.txt.enc'
output_file = 'example.txt'

with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

with open("salt.bin", "rb") as salt_file:
    salt = salt_file.read()

password = getpass.getpass("Enter decryption password: ").encode('utf-8')
key = generate_key(password, salt)

decrypt_file(input_file, output_file, key)
os.remove(input_file)
