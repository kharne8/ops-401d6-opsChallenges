#!/bin/python3

#Script: Ops 401 Class 03 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 19 APR 2023
#Purpose: In Python create an uptime sensor that uses ICMP packets to evaluate on the LAN are up or down.
#The script must:
# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

#Main

#import time for timestamp and ping3 / import smtplib
import time
import ping3
import smtplib
from email.mime.text import MIMEText

# Ask for user's email and password
senderEmail = input("Enter your email: ")
password = input("Enter your password: ")
receiverEmail = input("Enter the email address to receive notifications: ")

# Define function name / takes input ip address
def uptimeSensor(ipAddress):

    # set initial status to "None"
    oldStatus = "None"

    # set while loop to run forever every 2 secs
    while True:

        # set variable to store ping request
        response = ping3.ping(ipAddress, timeout=2)

        # if/else will change status depending on response
        if response is not None:
            status = "Active"
        else:
            status = "Inactive"

        # create stamp variable with the format needed
        timeStamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")

        # check if status has changed
        if status != oldStatus:
            # create email message
            msg = MIMEText(f"Network status for {ipAddress} changed from {oldStatus} to {status} at {timeStamp}")
            msg['Subject'] = f"Network status change for {ipAddress}"
            msg['From'] = senderEmail
            msg['To'] = receiverEmail

            # send email using SMTP library
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(sender_email, password)
                smtp.send_message(msg)

            # update previous status
            prev_status = status

        # print the timestamp, response status and ip address requested
        print(f"{timeStamp} Network status: {status} IP: {ipAddress}")

        # set run time for 2 secs
        time.sleep(2)

# run function with IP address input
uptimeSensor("8.8.8.8")
