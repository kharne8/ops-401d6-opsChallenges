#!/bin/python3

#Script: Ops 401 Class 16 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 8 May 2023
#Purpose: In Python, create a script that prompts the user to select one of the following modes:
#Mode 1: Offensive; Dictionary Iterator
#Mode 2: Defensive; Password Recognized

#Main

# Import libraries
import time, getpass

# Declare functions
def iterator():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    
    file = open(filepath, encoding="ISO-8859-1") # address encoding problem
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

def check_password():
    user_input = getpass.getpass(prompt="Enter the password to check: ")
    filepath = input("Enter the word list file path: ")
    try:
        with open(filepath, "r", encoding="ISO-8859-1") as wordlist:
            words = wordlist.readlines()
            for word in words:
                if user_input == word.strip():
                    print(f"Password found in the word list.")
                    return
        print(f"Password not found in the word list.")
    except FileNotFoundError:
        print(f"File not found at {filepath}")

# Main
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number: 
""")
        if mode == "1":
            iterator()
        elif mode == "2":
            check_password()
        elif mode == "3":
            break
        else:
            print("Invalid selection...")


#End
