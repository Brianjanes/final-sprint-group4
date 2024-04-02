# DESCRIPTION: This is a smaller program that will be brought into a larger program as a part of the Final Sprint for Semester 1. This program will start with a user input of the drivers number (or employee number) and return a report of their insurance policy informaton.
# AUTHOR: Brian Janes
# DATE: April 1st, 2024

import FormatValues as FV
import BrianJanesFunctions as BJanesFunc
import string

# ANSII escape codes to colour text in the terminal.
# Define ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"


def insurance_report():

    # Create an empty dictionary to store the employee data, and an empty list to store the employee data.
    # This makes the information earily iterable.
    employee = {}
    employee_data = []

    with open("employees.txt", "r") as f:
        # Skipping the headers in the line - Maybe this will be removed at some point
        next(f)
        for line in f:
            # Read the current employee list and split it into a list.
            # Using strip to remove any leading or trailing white space on the whole line.
            employee_list = line.strip().split(",")
            employee = {
                # Using strip() here to remove any leading or trailing white space on each element in the list.
                "driver_num": employee_list[0].strip(),
                "insurance_num": employee_list[1].strip(),
                "first_name": employee_list[2].strip(),
                "last_name": employee_list[3].strip(),
                # "address": employee_list[4].strip(),
                # "city": employee_list[5].strip(),
                # "province": employee_list[6].strip(),
                # "phone_num": employee_list[7].strip(),
                "license_num": employee_list[8].strip(),
                "insurance_company": employee_list[9].strip(),
                "own_car": employee_list[10].strip(),
                "balance": employee_list[11].strip()
            }
            employee_data.append(employee)

    # Formatting some stuff here before it is displayed.
    formatted_insurance_name = employee["insurance_company"].title()
    formatted_balance = FV.FDollar2(employee["balance"])
    formatted_name = employee["first_name"].title(
    ) + " " + employee["last_name"].title()

    # Removing address info - not sure if it's relevant for this.
    # formatted_phone_num = FV.format_phone_num(employee["phone_num"])
    # formatted_city = string.capwords(employee["city"])
    # formatted_address = string.capwords(employee["address"])
    # formatted_province = employee["province"].upper()
    formatted_license_num = employee["license_num"].upper()
    formatted_driver_num = employee["driver_num"]
    owns_car_display = "Yes" if employee["own_car"] == "Y" else "No"
    formatted_insurance_num = employee["insurance_num"].upper()

    # Starting with a validation loop to accept the proper parameters for a driver's license number. This is going to check for a 4 digit number. I will assume that this company will be using a 4 digit number for their drivers moving forward.
    while True:
        # Using a try // catch block to handle the user input - works very well for expected numerical inputs.
        try:
            # User input of the drivers number.
            print()
            driver_number = int(input("Please enter the drivers number: "))
            # Restricting the input to a 4 digit number.

            BJanesFunc.processing_blinker()

            # Looping through the employee data to find the driver number.
            for employee in employee_data:
                if employee["driver_num"] == str(driver_number):
                    print()
                    print(f"----------------------------------------")
                    print()
                    print(f"    Employee Insurance Information")
                    print()
                    print(f"   Insurance Company: {
                          formatted_insurance_name:<25s}")
                    print()
                    print(f"----------------------------------------")
                    print()
                    print(f"  Driver Name:          {formatted_name:<20s}")
                    print(f"  License Number:      {
                          formatted_license_num:<15s}")
                    print(f"  Driver Number:                  {
                          formatted_driver_num:>4s}")
                    print(f"  Insurance Number:              {
                          formatted_insurance_num:>5s}")
                    print()
                    print(f"  Owns Car:                        {
                          owns_car_display:<3s}")
                    print(f"  Balance:                  {
                          formatted_balance:>10}")
                    print()
                    print(f"----------------------------------------")
                    print()
                    return  # Exit the function after successful validation
            # If the loop completes without finding a matching driver number
            print(
                f"{RED}  Data Entry Error - Driver not found, please try again.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")


insurance_report()
