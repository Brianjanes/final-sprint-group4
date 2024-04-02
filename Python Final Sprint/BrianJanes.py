# DESCRIPTION: This is a smaller program that will be brought into a larger program as a part of the Final Sprint for Semester 1. This program will start with a user input of the drivers number (or employee number) and return a report of their insurance policy informaton.
# AUTHOR: Brian Janes
# DATE: April 1st, 2024

import FormatValues as FV


def insurance_report():
    # Starting with a validation loop to accept the proper parameters for a driver's livense number.
    while True:
        try:
            # User input of the drivers number.
            driver_number = int(input("Please enter the drivers number: "))
            # Restricting the input to a 4 digit number.
            if driver_number < 1000 or driver_number > 9999:
                print(
                    "Data Entry Error - Invalid input. Please input a valid driver number. (1000-9999)")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Need to find te driver dictionary that matches the driver number.
    # Then I will deconstruct the information about the insurance policy of the driver & display it.


# Example dictionary structure to be used for the report.
insurance_dict = {
    "policy_num": 1234,
    "company": "State Farm",
    "driver_name": "John Doe",
    "monthly_rate": 100,
    "deductable": 500,
}

# Example information to add to the .dat file.
insurance_company_name = "ABC Insurance"
insurance_policy_num = 5678
driver_name = "Jane Smith"
insurance_rate = 150
insurance_deductable = 1000

# Add this to the .dat file as this dictionary will be used to create the report.
insurance_dict.append({
    "company": insurance_company_name,
    "policy_num": insurance_policy_num,
    "driver_name": driver_name,
    "monthly_rate": insurance_rate,
    "deductable": insurance_deductable
})

driver_name, policy_num, company, monthly_rate, deductable = insurance_dict

formatted_deductible = FV.dollar2(deductable)
formatted_monthly_rate = FV.dollar2(monthly_rate)

# This will be the final report that will be displayed to the user.
print()
print("  Insurance Policy Report")
print("---------------------------")

print(f"Company: {company}")
print(f"Driver Number: {driver_name:<20s}")
print(f"Policy Number: {policy_num:>4s}")
print()
print(f"Monthly Rate: {formatted_monthly_rate}")
print(f"Deductable: {formatted_deductible:>10s}")
# End of program.
