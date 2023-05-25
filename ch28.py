#!/bin/python

#Script: Ops 401 Class 28 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 24 MAY 2023
#Purpose: 

#Main

import logging
from logging.handlers import RotatingFileHandler
import sys

# Configure the logger with a rotating file handler
log_file = 'script.log'
# Maximum size of each log file in bytes
max_bytes = 1024
# Number of backup log files to keep
backup_count = 5

# FileHandler should write to a local file
file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# StreamHandler should output to the terminal
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# Create a logger and add the handlers
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def print_syslog_lines():
    # Read the syslog file
    with open('/var/log/syslog', 'r') as syslog_file:
        lines = syslog_file.readlines()

    num_lines = len(lines)
    current_line = 0

    # Print the first 10 lines
    for line in lines[current_line:current_line + 10]:
        print(line.strip())

    current_line += 10

    # Prompt the user to continue printing
    while current_line < num_lines:
        user_input = input("Press Enter to print the next 10 lines (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        # Print the next 10 lines
        for line in lines[current_line:current_line + 10]:
            print(line.strip())

        current_line += 10

        # Log each usage of the function
        logger.info("Printed lines from syslog. Current line: %d", current_line)

    print("Exiting...")


print_syslog_lines()


#End
