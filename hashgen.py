import hashlib

def generate_hash(text, algorithm):
    if algorithm == 1:
        hash_obj = hashlib.md5()
    elif algorithm == 2:
        hash_obj = hashlib.sha1()
    elif algorithm == 3:
        hash_obj = hashlib.sha224()
    elif algorithm == 4:
        hash_obj = hashlib.sha256()
    elif algorithm == 5:
        hash_obj = hashlib.sha384()
    elif algorithm == 6:
        hash_obj = hashlib.sha512()
    else:
        print("Invalid option!")
        return None
    
    hash_obj.update(text.encode('utf-8'))
    return hash_obj.hexdigest()

def main():
    print("Choose a hashing algorithm:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA224")
    print("4. SHA256")
    print("5. SHA384")
    print("6. SHA512")
    algorithm = int(input("Enter the number of the hashing algorithm: "))
    text = input("Enter a string to hash: ")
    hashed_value = generate_hash(text, algorithm)
    if hashed_value:
        print(f"Hash value: {hashed_value}")

if __name__ == "__main__":
    main()
