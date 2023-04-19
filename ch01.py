#!/bin/python3

#Script: Ops 401 Class 02 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 18 APR 2023
#Purpose: In Python create an uptime sensor that uses ICMP packets to evaluate on the LAN are up or down.
#The script must:
# Transmit a single ICMP(ping) packet to a specific IP every two seconds
# Evaluate the response as either success or failure
# Assign success or failure status variable
# For every ICMP transsmission attempted, print the status variable along with a
# comprehensive timestamp and destination IP tested

#Main

#import time for timestamp and ping3 
import time
import ping3

# Define function name / takes input ip address
def uptimeSensor(ipAddress):
    
    #set while loop to run forever every 2 secs
    while True:
        status = "None"

        # set variable to store ping request
        response = ping3.ping(ipAddress, timeout=2)

        # if/else will change status depeending on response
        if response is not None:
            status = "Active"
        else:
            status = "Inactive"

        # create stamp variable with the format needed
        timeStamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")

        # print the timestamp, response status and ip address requested
        print(f"{timeStamp} Network status: {status} IP: {ipAddress}")

        # set run time for 2 secs
        time.sleep(2)

uptimeSensor("8.8.8.8")

#End