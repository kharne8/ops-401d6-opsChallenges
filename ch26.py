import logging

logging.basicConfig(filename='script.log', level=logging.INFO)

def print_syslog_lines():
    # Read the syslog file
    with open('/var/log/syslog', 'r') as syslog_file:
        lines = syslog_file.readlines()

    num_lines = len(lines)
    current_line = 0

    # Print the first 10 lines
    for line in lines[current_line:current_line+10]:
        print(line.strip())

    current_line += 10

    # Prompt the user to continue printing
    while current_line < num_lines:
        user_input = input("Press Enter to print the next 10 lines (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        # Print the next 10 lines
        for line in lines[current_line:current_line+10]:
            print(line.strip())

        current_line += 10

        # Log each usage of the function
        logging.info("Printed lines from syslog. Current line: %d", current_line)

    print("Exiting...")

print_syslog_lines()
