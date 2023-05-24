#!/bin/python3

#Script: Ops 401 Class 27 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 23 May 2023
#Purpose: Add a log rotation feature based on size to ch26 python script

#Main

import logging
from logging.handlers import RotatingFileHandler

#configure the logger with a rotating file handler
log_file = 'script.log'
#maximum size of each log file in bytes
max_bytes = 1024  
#number of backup log files to keep
backup_count = 5  
handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
handler.setLevel(logging.INFO)

#create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

#create a logger and add the handler
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def print_syslog_lines():
    # Read the syslog file
    with open('/var/log/syslog', 'r') as syslog_file:
        lines = syslog_file.readlines()

    num_lines = len(lines)
    current_line = 0

    #print the first 10 lines
    for line in lines[current_line:current_line + 10]:
        print(line.strip())

    current_line += 10

    #prompt the user to continue printing
    while current_line < num_lines:
        user_input = input("Press Enter to print the next 10 lines (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        #print the next 10 lines
        for line in lines[current_line:current_line + 10]:
            print(line.strip())

        current_line += 10

        #log each usage of the function
        logger.info("Printed lines from syslog. Current line: %d", current_line)

    print("Exiting...")


print_syslog_lines()

#End
