import os
from cryptography.fernet import Fernet

# This code does the reverse of encrypt.py

# Name of the secret key
unlock_key = "unlocker.key"

files = []

# Looks at all the files in the current directory
# Adds it to the files list
for file in os.listdir():

    if file == "encrypt.py" or file == unlock_key or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)
print(files)

# Reads the current unlocking key
with open(unlock_key, "rb") as key:
    secret_key = key.read()

# Reads through all the files in the files list
for file in files:

    # Opens and reads the file
    with open(file, "rb") as selected_file:
        content = selected_file.read()

    # Encrypts the file's content
    content_decrypted = Fernet(secret_key).decrypt(content)

    # Applies changes to the file
    with open(file, "wb") as selected_file:
        selected_file.write(content_decrypted)
