#!/bin/python

#Script: Ops 401 Class 36 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 7 JUN 2023
#Purpose: In Python create a script that executes from a Linux box to perform the following:
  ## Prompts the user to type a URL or IP address.
  ## Prompts the user to type a port number.
  ## Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
  ## Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
  ## Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.


#Main
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

#End
