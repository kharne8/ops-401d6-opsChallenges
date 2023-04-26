#!/bin/python3

#Script: Ops 401 Class 06 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 24 APR 2023
#Purpose: In Python, create a script that utilizes the cryptography library to:
#Prompt the user to select a mode:
# If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# Encrypt a file (mode 1)
# Decrypt a file (mode 2)
# If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
# Encrypt a message (mode 3)
# Decrypt a message (mode 4)



#Main

#import cryptography module to handle encryption and decryption, and the os module to delete the key file after each operation.
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
def encrypt_file(filename):
    """
    Encrypts a file
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        #encrypts the file
        encrypted_data = f.encrypt(file_data)
    
    #replaces the original file with the encrypted version
    with open(filename, "wb") as file:
        file.write(encrypted_data)

#decrypt_file function takes a file path and a key as input
def decrypt_file(filename, key):
    """
    Decrypts a file
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        #decrypts the file
        decrypted_data = f.decrypt(encrypted_data)
    
    #replaces the encrypted file with the decrypted version
    with open(filename, "wb") as file:
        file.write(decrypted_data)

#encrypt_message function takes a string message and a key as input
def encrypt_message(message, key):
    """
    Encrypts a message
    """
    f = Fernet(key)
    #encrypts the message
    encrypted_message = f.encrypt(message.encode())
    
    #prints the encrypted message to the console
    print(f"Encrypted message: {encrypted_message.decode()}")

#decrypt_message function takes an encrypted string message and a key as input
def decrypt_message(message, key):
    """
    Decrypts a message
    """
    f = Fernet(key)
    #decrypts the message
    decrypted_message = f.decrypt(message.encode())
    
    #prints the decrypted message to the console
    print(f"Decrypted message: {decrypted_message.decode()}")


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
        
    elif mode == "3":
        message = input("Enter the message you want to encrypt: ")
        get_key()
        key = load_key()
        encrypt_message(message, key)
        os.remove("key.key")
        
    elif mode == "4":
        message = input("Enter the message you want to decrypt: ")
        get_key()
        key = load_key()
        decrypt_message(message, key)
        os.remove("key.key")
        
    else:
        print("Invalid mode.")
        
if __name__ == "__main__":
    main()

#End
#
