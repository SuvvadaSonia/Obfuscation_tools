from cryptography.fernet import Fernet
import os

# Generate a key for encryption
key = Fernet.generate_key()
print(key)

# Walk through the directory and encrypt each file
def encrypt_file(filename: str, key: bytes) -> None:
    with open(filename, "rb") as f:
        data = f.read()     # Open the file and read its contents

    fernet = Fernet(key)    # Initialize the Fernet encryption object with the key
    encrypted_data = fernet.encrypt(data)  # Encrypt the contents using Fernet

    with open(filename, "wb") as f:
        f.write(encrypted_data)     # Write the encrypted contents back to the file 

def encrypt_folder(foldername: str, key: bytes) -> None:
    for root, dirs, files in os.walk(foldername):
        for filename in files:
            encrypt_file(os.path.join(root, filename), key)
            
# Define the path to the folder you want to encrypt          
encrypt_folder("C:/Users/sonia.s/Desktop/encryption/Sample_copy", key)

print("Encrypted Successfully")

# key = DXtdB-Gsj3lUMawwFxdzHm79xhQOT_0putVvt6UzMJw=
