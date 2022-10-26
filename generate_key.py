from cryptography.fernet import Fernet

def generateKey(key_file):
    key = Fernet.generate_key()

    with open(key_file,'wb') as file:
        file.write(key)
key_file = input("Enter path to save key file: ")
key_file = key_file + '\key.key'
generateKey(key_file)
