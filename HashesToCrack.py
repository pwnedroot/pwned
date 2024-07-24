

import hashlib
import random
import string
import pyfiglet  # Import the pyfiglet library

# Function to generate a random string of variable length
def generate_random_string(length, include_special_chars=True):
    if include_special_chars:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a random password and its hashes
def generate_password_and_hashes(easy_mode=False, include_special_chars=True):
    if easy_mode:
        easy_passwords = ["123456", "test123", "admin", "password", "letmein", "qwerty"]
        random_password = random.choice(easy_passwords)
        length = len(random_password)
        random_string = random_password
    else:
        length = random.randint(6, 16)  # Generate random length between 6 and 16
        random_string = generate_random_string(length, include_special_chars)

    md5_hash = hashlib.md5(random_string.encode()).hexdigest()
    sha256_hash = hashlib.sha256(random_string.encode()).hexdigest()
    return random_string, md5_hash, sha256_hash

# Main function to demonstrate
if __name__ == "__main__":
    # Generate ASCII art header with "HashCrack"
    ascii_art = pyfiglet.figlet_format("HashCrack")
    print(ascii_art)

    # Ask user if they want to use special characters
    special_chars_input = input("Do you want to include special characters? (yes/no): ").strip().lower()
    include_special_chars = special_chars_input == "yes"

    # Ask user if they want to use easy mode
    easy_mode_input = input("Do you want to use easy mode? (yes/no): ").strip().lower()
    easy_mode = easy_mode_input == "yes"

    # Generate random password and hashes
    random_string, md5_hash, sha256_hash = generate_password_and_hashes(easy_mode, include_special_chars)

    print(f"Generated Password: {'*' * len(random_string)}")
    print(f"MD5 Hash: {md5_hash}")
    print(f"SHA-256 Hash: {sha256_hash}")
    print()

    show_password = input("Do you want to see the plaintext password? (yes/no): ").strip().lower()
    if show_password == "yes":
        print(f"\nPlaintext Password: {random_string}")
