from cryptography.fernet import Fernet
import os
import subprocess

# Path to the Python script you want to run
script_path = "C:/Users/sonia.s/Desktop/encryption/Sample_copy/main.py"

# Prompt the user for the key used to encrypt the folder
key = input("Enter the key used to encrypt the folder: ")

# Walk through the directory and decrypt each file
def decrypt_file(filename: str, key: bytes) -> None:
    with open(filename, "rb") as f:
        data = f.read()   # Open the encrypted file and read its contents

    fernet = Fernet(key)   # Initialize the Fernet encryption object with the key
    decrypted_data = fernet.decrypt(data)  # Decrypt the contents using Fernet

    with open(filename, "wb") as f:
        f.write(decrypted_data)    # Write the decrypted contents back to the file
                 

def decrypt_folder(foldername: str, key: bytes) -> None:
    for root, dirs, files in os.walk(foldername):
        for filename in files:
            decrypt_file(os.path.join(root, filename), key)
            
    
# Define the path to the folder you want to decrypt
decrypt_folder("C:/Users/sonia.s/Desktop/encryption/Sample_copy", key)

print("Folder decryption complete!")

# Execute the file using the subprocess module
subprocess.call(['python', script_path])



def encrypt_file(filename: str, key: bytes) -> None:
    with open(filename, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(filename, "wb") as f:
        f.write(encrypted_data)

def encrypt_folder(foldername: str, key: bytes) -> None:
    for root, dirs, files in os.walk(foldername):
        for filename in files:
            encrypt_file(os.path.join(root, filename), key)
            

encrypt_folder("C:/Users/sonia.s/Desktop/encryption/Sample_copy", key)

print("Encrypted successfully after execution")
            