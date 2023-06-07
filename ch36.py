import os
import subprocess

# Function to perform banner grabbing using netcat
def netcat_banner_grabbing(target_address, port):
    try:
        output = subprocess.check_output(['nc', '-vz', '-w', '2', target_address, str(port)], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

# Function to perform banner grabbing using telnet
def telnet_banner_grabbing(target_address, port):
    try:
        output = subprocess.check_output(['telnet', target_address, str(port)], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

# Function to perform banner grabbing using Nmap
def nmap_banner_grabbing(target_address):
    try:
        output = subprocess.check_output(['nmap', '-sV', target_address], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode())

# Prompt user for input
target_address = input("Enter the target URL or IP address: ")
port = int(input("Enter the target port number: "))

# Perform banner grabbing using netcat
print("Banner grabbing using netcat:")
netcat_banner_grabbing(target_address, port)
print()

# Perform banner grabbing using telnet
print("Banner grabbing using telnet:")
telnet_banner_grabbing(target_address, port)
print()

# Perform banner grabbing using Nmap
print("Banner grabbing using Nmap:")
nmap_banner_grabbing(target_address)
