#!/usr/bin/env python3

#Script: Ops 401 Class 23 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 2 May 2023
#Purpose: Add the following features to ch12.py
#In Python, combine the two modes (port and ping) of your network scanner script.
#Eliminate the choice of mode selection.
#Continue to prompt the user for an IP address to target.
#Move port scan to its own function.
#Call the port scan function if the host is responsive to ICMP echo requests.
#Print the output to the screen.


#Main

#import modules
import os
import sys
import socket
import struct
from scapy.all import *

#function to calculate subnet mask from CIDR notation
def cidrToSubnet(cidr):
    subnetBits = 0xffffffff ^ (1 << 32 - int(cidr)) - 1
    subnet = socket.inet_ntoa(struct.pack('>I', subnetBits))
    return subnet

#function to generate list of IP addresses in a network
def generateIPList(network):
    IPList = []
    for ip in IPNetwork(network):
        IPList.append(str(ip))
    return IPList

#fuction to scan ports
def scanPorts(targetHost, portRange):
    openPorts = []
    for port in portRange:
        synPacket = IP(dst=targetHost)/TCP(dport=port, flags="S")
        response = sr1(synPacket, timeout=1, verbose=0)

        if response is not None and response.haslayer(TCP) and response[TCP].flags == 0x12:
            rstPacket = IP(dst=targetHost)/TCP(dport=port, flags="R")
            send(rstPacket, verbose=0)
            openPorts.append(port)

        elif response is not None and response.haslayer(TCP) and response[TCP].flags == 0x14:
            pass

        else:
            pass

    return openPorts

#function to ping a host and scan ports if it's up
def pingAndScan(ip):
    ping = IP(dst=ip)/ICMP()
    response = sr1(ping, timeout=2, verbose=False)
    if response is None:
        print(f"{ip} is down or unresponsive.")
    elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
        print(f"{ip} is actively blocking ICMP traffic.")
    else:
        print(f"{ip} is responding. Scanning for open ports...")
        portRange = range(1, 1025)
        openPorts = scanPorts(ip, portRange)
        if openPorts:
            print(f"Open ports: {openPorts}")
        else:
            print("No open ports found.")

#main program
while True:
    targetHost = input("Enter the IP address to target (e.g. 192.168.0.1): ")
    pingAndScan(targetHost)

#End
