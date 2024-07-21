from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import hashlib
import os

# Function to generate a secure key using PBKDF2
def generate_key(password):
    salt = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=32)
    return key, salt

# Function to encrypt a file
def encrypt_file(input_file, output_file, password):
    key, salt = generate_key(password)
    cipher = AES.new(key, AES.MODE_CBC)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)
        f.write(salt)
        f.write(ciphertext)

# Function to decrypt a file
def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        salt = f.read(16)
        ciphertext = f.read()
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(output_file, 'wb') as f:
        f.write(plaintext)

# Menu function to choose encryption or decryption
def menu():
    print("Choose an option:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter your choice (1 or 2): ").strip()
    return choice

# Example usage
if __name__ == "__main__":
    choice = menu()

    if choice == '1':
        input_file = input("Enter path to the file to encrypt: ").strip()
        encrypted_file = 'encrypted.bin'
        password = input("Enter password for encryption: ")

        encrypt_file(input_file, encrypted_file, password)
        print(f'File {input_file} encrypted to {encrypted_file}')

    elif choice == '2':
        input_file = input("Enter path to the file to decrypt: ").strip()
        decrypted_file = 'decrypted.txt'
        password = input("Enter password for decryption: ")

        decrypt_file(input_file, decrypted_file, password)
        print(f'File {input_file} decrypted to {decrypted_file}')

    else:
        print("Invalid choice. Please enter 1 or 2.")
