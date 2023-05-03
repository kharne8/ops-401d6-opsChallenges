#!/bin/python3

#Script: Ops 401 Class 07 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 25 APR 2023
#Purpose: In Python, update ch6 script to accomplish the following:
#Recursively encrypt a single folder and all its contents.
#Recursively decrypt a single folder that was encrypted by this tool.


#Main

#import modules
from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_key():
    """Generates a new key and saves it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the key file."""
    try:
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print(f"Key file {KEY_FILE} not found.")
    except ValueError:
        print(f"Invalid key in file {KEY_FILE}.")

def encrypt_file(filepath, key):
    """Encrypts a file or directory and its contents recursively."""
    if os.path.isfile(filepath):
        with open(filepath, "rb") as file:
            file_data = file.read()
        f = Fernet(key)
        encrypted_data = f.encrypt(file_data)
        with open(filepath, "wb") as file:
            file.write(encrypted_data)
        print(f"File {filepath} encrypted.")
    elif os.path.isdir(filepath):
        for root, dirs, files in os.walk(filepath):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)
    else:
        print(f"Invalid file path {filepath}.")

def decrypt_file(filepath, key):
    """Decrypts a file or directory and its contents recursively."""
    if os.path.isfile(filepath):
        with open(filepath, "rb") as file:
            encrypted_data = file.read()
        f = Fernet(key)
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except ValueError:
            print(f"Unable to decrypt file {filepath}.")
        else:
            with open(filepath, "wb") as file:
                file.write(decrypted_data)
            print(f"File {filepath} decrypted.")
    elif os.path.isdir(filepath):
        for root, dirs, files in os.walk(filepath):
            for file in files:
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
    else:
        print(f"Invalid file path {filepath}.")

def main():
    print("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message")
    mode = input("Mode: ")
    if mode == "1":
        filepath = input("Enter the filepath to the file you want to encrypt: ")
        if not os.path.isfile(filepath):
            print(f"Invalid file path {filepath}.")
            return
        generate_key()
        key = load_key()
        if key:
            encrypt_file(filepath, key)
            print("File encrypted.")
            os.remove(KEY_FILE)
    elif mode == "2":
        filepath = input("Enter the filepath to the file you want to decrypt: ")
        if not os.path.isfile(filepath):
            print(f"Invalid file path {filepath}.")
            return
        key = load_key()
        if key:
            decrypt_file(filepath, key)
            print("File decrypted.")
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()

#End
