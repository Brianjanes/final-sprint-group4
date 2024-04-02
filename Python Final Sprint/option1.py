# Enter a new driver 
# by Brian Jackman
# 2024 04 01 - 2024 04 02 


#function for inputs and validations
def driver_input():
    while True:
        DrivNum = input("Enter the driver number: ")
        allowed_char = set("1234567890")
        if DrivNum == "":
            print("Data Entry Error - Driver number cannot be blank.")
        elif set(DrivNum).issubset(allowed_char) == False:
            print("Data Entry Error - Driver number contains invalid characters.")
        else:
            break
    
    print()
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
        DrivFirName = input("Enter the driver's first name: ").title()
        if DrivFirName == "":
            print("Data Entry Error - Driver's first name cannot be blank.")
        elif set(DrivFirName).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's first name contains invalid characters.")
        else:
            break
    print()

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
        DrivLasName = input("Enter the driver's last name: ").title()
        if DrivLasName == "":
            print("Data Entry Error - Driver's last name cannot be blank.")
        elif set(DrivLasName).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's last name contains invalid characters.")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
        DrivAddress = input("Enter the driver's address: ").upper()
        if DrivAddress == "":
            print("Data Entry Error - Driver's address cannot be blank.")
        elif set(DrivAddress).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's address contains invalid characters.")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrstuvwxyz")
        DrivPostCode = input("Enter the driver's postal code: ").upper()
        if DrivPostCode == "":
            print("Data Entry Error - Driver's postal code cannot be blank.")
        elif set(DrivPostCode).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's postal code contains invalid characters.")
        elif len(DrivPostCode) != 6:
            print("Data Entry Error - Driver's postal code must be 6 digits")
        else:
            break
    print()

    while True:
        allowed_char = set("123456789-")
        DrivPhonNum = input("Enter the driver's phone number(999-999-9999): ")
        if DrivPhonNum == "":
            print("Data Entry Error - Driver's phone number cannot be blank.")
        elif set(DrivPhonNum).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's phone number contains invalid characters.")
        elif len(DrivPhonNum) != 12:
            print("Data Entry Error - Driver's phone number must be in format 999-999-9999.")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrstuvwxyz")
        DrivLicNum = input("Enter the driver's licence number: ")
        if DrivLicNum == "":
            print("Data Entry Error - Driver's license number cannot be blank.")
        elif set(DrivLicNum).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's license number contains invalid characters.")
        elif len(DrivLicNum) not in [7, 8]:
            print("Data Entry Error - Driver's license number must be 7 or 8 digits")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890-")
        DrivLicExpDate = input("Enter the driver licence expiry date: (YYYY-MM-DD): ")
        if DrivLicExpDate == "":
            print("Data Entry Error - Driver's license expiry date cannot be blank.")
        elif set(DrivLicExpDate).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's license expiry date contains invalid characters.")
        elif len(DrivLicExpDate) != 10:
            print("Data Entry Error - Driver's license expiry date must be in format YYYY-MM-DD")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrstuvwxyz -.")
        InsurComp = input("Enter the insurance company they are insured with: ").title()
        if InsurComp == "":
            print("Data Entry Error - Driver's insurance company cannot be blank.")
        elif set(InsurComp).issubset(allowed_char) == False:
            print("Data Entry Error - Driver's insurance company contains invalid characters.")
        else:
            break
    print()

    while True:
        Rental = input("Do they need a rental car?(Y/N): ").upper()
        if Rental == "":
            print("Data Entry Error - Must select Y or N.")
        elif Rental != "Y" and Rental != "N":
            print("Data Entry Error - Must select Y or N.")
        else:
            break
# save inputs to data file
    z = open("DriverInfo.dat", "a")
    z.write("{}, ".format((DrivNum)))
    z.write("{}, ".format(DrivFirName))
    z.write("{}, ".format(DrivLasName))
    z.write("{}, ".format(DrivAddress))
    z.write("{}, ".format(DrivPostCode))
    z.write("{}, ".format(DrivPhonNum))
    z.write("{}, ".format(DrivLicNum))
    z.write("{}, ".format(DrivLicExpDate))
    z.write("{}, ".format(InsurComp))
    z.write("{}, ".format(Rental))
    z.close()
print()
print("Data Saved")
#run function and ask if want to run it again
driver_input()
while True:
    allowed_char = set("YNyn")
    RunAgain = input("Would you like to enter another driver's information(Y/N)?: ").upper()
    print()
    if RunAgain =="":
        print("Data Entry Error - Cannot be blank")
    elif set(RunAgain).issubset(allowed_char) == False:
        print("Data Entry Error - Must enter Y or N")
    elif RunAgain == "Y":
        driver_input()
    else:
        break
