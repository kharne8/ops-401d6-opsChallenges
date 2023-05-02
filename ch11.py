#!/bin/python3

#Script: Ops 401 Class 11 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 1 May 2023
#Purpose: In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
# Utilize the scapy library
# Define host IP
# Define port range or specific set of ports to scan
# Test each port in the specified range using a for loop
# If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
# If flag 0x14 received, notify user the port is closed.
# If no flag is received, notify the user the port is filtered and silently dropped.

#Main

#!/usr/bin/env python3

#import scapy
from scapy.all import *

#define the target host IP
targetHost = "scanme.nmap.org"

#define the port range to scan
portRange = range(1, 1025)

#loop over the port range and check each port
for port in portRange:

    #store SYN packet in a variable and send it to the target host
    synPacket = IP(dst=targetHost)/TCP(dport=port, flags="S")
    response = sr1(synPacket, timeout=1, verbose=0)

    #check if the response is not None and if it has the SYN/ACK flag set
    if response is not None and response.haslayer(TCP) and response[TCP].flags == 0x12:
        #dend a RST packet to close the connection
        rstPacket = IP(dst=target_Host)/TCP(dport=port, flags="R")
        send(rstPacket, verbose=0)
        print("Port {} is open".format(port))

    #check if the response is not None and if it has the RST flag set
    elif response is not None and response.haslayer(TCP) and response[TCP].flags == 0x14:
        print("Port {} is closed".format(port))

    # Otherwise, assume the port is filtered
    else:
        print("Port {} is filtered".format(port))

#End
