#!/usr/bin/env python3

#Script: Ops 401 Class 23 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 2 May 2023
#Purpose: Add the following features to ch11.py
# Add user menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode,
# Create an ICMP Ping Sweep tool that:
# 1. Prompt user for network address including CIDR block, for example “10.10.0.0/24”. Careful not to populate the host bits!
# 2. Create a list of all addresses in the given network
# 3. Ping all addresses on the given network except for network address and broadcast address
# 4. If no response, inform the user that the host is down or unresponsive.
# 5. If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
# 6.Otherwise, inform the user that the host is responding.

#Main

#import modules
import os
import sys
import socket
import struct
from scapy.all import *

#function to calculate subnet mask from CIDR notation
def cidrToSubnet(cidr):
    subnet_bits = 0xffffffff ^ (1 << 32 - int(cidr)) - 1
    subnet = socket.inet_ntoa(struct.pack('>I', subnet_bits))
    return subnet

#function to generate list of IP addresses in a network
def generate_IPList(network):
    IPList = []
    for ip in IPNetwork(network):
        IPList.append(str(ip))
    return IPList

#fnction to ping a host
def pingHost(ip):
    ping = IP(dst=ip)/ICMP()
    response = sr1(ping, timeout=2, verbose=False)
    if response is None:
        print(f"{ip} is down or unresponsive.")
    elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
        print(f"{ip} is actively blocking ICMP traffic.")
    else:
        print(f"{ip} is responding.")

#fuction to scan ports
def scanPorts(targetHost, portRange):
    open_ports = []
    for port in portRange:
        synPacket = IP(dst=targetHost)/TCP(dport=port, flags="S")
        response = sr1(synPacket, timeout=1, verbose=0)

        if response is not None and response.haslayer(TCP) and response[TCP].flags == 0x12:
            rstPacket = IP(dst=targetHost)/TCP(dport=port, flags="R")
            send(rstPacket, verbose=0)
            open_ports.append(port)

        elif response is not None and response.haslayer(TCP) and response[TCP].flags == 0x14:
            pass

        else:
            pass

    print(f"Open ports: {open_ports}")

#Main menu
while True:
    print("\nMENU")
    print("1. Ping sweep")
    print("2. Port scan")
    print("3. Quit")
    choice = input("\nEnter your choice: ")

    if choice == '1':
        # Ping sweep
        network_cidr = input("Enter the network address in CIDR notation (e.g. 10.10.0.0/24): ")
        subnet_mask = cidrToSubnet(network_cidr.split('/')[1])
        IPList = generate_IPList(network_cidr)
        IPList.remove(str(IPAddress(network_cidr.split('/')[0])))
        IPList.remove(str(IPAddress(network_cidr.split('/')[0] | (~int(subnet_mask) & 0xFFFFFFFF))))
        for ip in IPList:
            pingHost(ip)

    elif choice == '2':
        # Port scan
        targetHost = input("Enter the target host: ")
        portRange = range(1, 1025)
        scanPorts(targetHost, portRange)

    elif choice == '3':
        # Quit
        sys.exit()

    else:
        print("Invalid choice. Please try again.")

#End
