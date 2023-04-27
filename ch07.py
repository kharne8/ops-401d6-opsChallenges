#!/bin/python3

#Script: Ops 401 Class 07 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 25 APR 2023
#Purpose: In Python, update ch6 script to accomplish the following:
#Recursively encrypt a single folder and all its contents.
#Recursively decrypt a single folder that was encrypted by this tool.


#Main

from cryptography.fernet import Fernet
import os

#define a get_key function that generates a key and saves it to a file named key.key
def get_key():
    """
    Generates a key and saves it to a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

        
#define a load_key function that loads the key from the key.key file        
def load_key():
    """
    Loads the previously generated key
    """
    return open("key.key", "rb").read()

#encrypt_file function takes a file path and a key as input
def encrypt_file(filepath):
    """
    Encrypts a file or directory and its contents recursively
    """
    #generate and load the encryption key
    get_key()
    key = load_key()
    
    if os.path.isfile(filepath):
        
        #if the input path is a file, encrypt it
        f = Fernet(key)
        with open(filepath, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        with open(filepath, "wb") as file:
            file.write(encrypted_data)
        print(f"File {filepath} encrypted.")
    elif os.path.isdir(filepath):
        
        #if the input path is a directory, recursively encrypt all files within it
        for root, dirs, files in os.walk(filepath):
            for file in files:
                file_path = os.path.join(root, file)
                f = Fernet(key)
                with open(file_path, "rb") as file:
                    file_data = file.read()
                    encrypted_data = f.encrypt(file_data)
                with open(file_path, "wb") as file:
                    file.write(encrypted_data)
                print(f"File {file_path} encrypted.")
    else:
        print("Invalid file path.")
        return
    os.remove("key.key")
    
    #decrypt_file function takes a file path and a key as input
    def decrypt_file(filepath, key):
    """
    Decrypts a file or directory and its contents recursively
    """
    if os.path.isfile(filepath):
        # if the input path is a file, decrypt it
        f = Fernet(key)
        with open(filepath, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
        with open(filepath, "wb") as file:
            file.write(decrypted_data)
        print(f"File {filepath} decrypted.")
    elif os.path.isdir(filepath):
        # if the input path is a directory, recursively decrypt all files within it
        for root, dirs, files in os.walk(filepath):
            for file in files:
                file_path = os.path.join(root, file)
                f = Fernet(key)
                with open(file_path, "rb") as file:
                    encrypted_data = file.read()
                    decrypted_data = f.decrypt(encrypted_data)
                with open(file_path, "wb") as file:
                    file.write(decrypted_data)
                print(f"File {file_path} decrypted.")
    else:
        print("Invalid file path.")
        return


#prompts the user to select a mode => then calls the function based on selection
def main():
    print("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message")
    mode = input("Mode: ")
    
    if mode == "1":
        filepath = input("Enter the filepath to the file you want to encrypt: ")
        if not os.path.isfile(filepath):
            print("Invalid file path.")
            return
        get_key()
        key = load_key()
        encrypt_file(filepath, key)
        print("File encrypted.")
        os.remove("key.key")
        
    elif mode == "2":
        filepath = input("Enter the filepath to the file you want to decrypt: ")
        if not os.path.isfile(filepath):
            print("Invalid file path.")
            return
        get_key()
        key = load_key()
        decrypt_file(filepath, key)
        print("File decrypted.")
        os.remove("key.key")
        
    else:
        print("Invalid mode.")
        
if __name__ == "__main__":
    main()

#End
