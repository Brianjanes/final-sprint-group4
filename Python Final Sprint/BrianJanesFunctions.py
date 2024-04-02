import time
import sys

# ANSII escape codes to colour text in the terminal.
# Define ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"


def processing_blinker():
    """
    A short blinking statement to pause inbetween inputs to create a better flow for the user.
    """
    print()
    # Change to control number of 'blinks'
    for _ in range(2):
        print(f"{GREEN}    Retrieving Policy Information...{RESET}", end="\r")
        # Pause for 0.3 seconds
        time.sleep(0.3)
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)
