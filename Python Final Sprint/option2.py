#Enter company revenues 
# by Brian Jackman
# 2024 04 02


#function for inputs and validations
def transaction_input():
    while True:
        allowed_char = set("1234567890")
        TransID = input("Enter the transaction ID: ")
        if TransID == "":
            print("Data Entry Error - Transaction ID cannot be blank.")
        elif set(TransID).issubset(allowed_char) == False:
            print("Data Entry Error - Transaction ID contains invalid characters.")
        else:
            break

    while True:
        allowed_char = set("1234567890")
        DrivNum = input("Enter the driver number: ")
        if DrivNum == "":
            print("Data entry error - Driver number cannot be blank.")
        elif set(DrivNum).issubset(allowed_char) == False:
            print("Data Entry Error - Driver number contains invalid characters.")
        else:
            break

    while True:
        allowed_char = set("1234567890-")
        TransDate = input("Enter the transaction date (YYYY-MM-DD): ")
        if TransDate == "":
            print("Data Entry Error - Transaction date cannot be blank.")
        elif set(TransDate).issubset(allowed_char) == False:
            print("Data Entry Error - Transaction date contains invalid characters.")
        elif len(TransDate) != 10:
            print("Data Entry Error - Transaction date must be in format YYYY-MM-DD")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
        TransDesc = input("Enter the transaction description: ").title()
        if TransDesc == "":
            print("Data Entry Error - Transaction description cannot be blank.")
        elif set(TransDesc).issubset(allowed_char) == False:
            print("Data Entry Error - Transaction description contains invalid characters.")
        else:
            break

    while True:
        allowed_char = set("1234567890.")
        TransAmount = input("Enter the transaction amount: ")
        if TransAmount == "":
            print("Data Entry Error - Transaction amount cannot be blank.")
        elif set(TransAmount).issubset(allowed_char) == False:
            print("Data Entry Error - Transaction amount contains invalid characters.")
        else:
            break

    while True:
        allowed_char = set("1234567890.")
        TransHST = input("Enter the transaction HST: ")
        if TransHST == "":
            print("Data Entry Error - Transaction hit cannot be blank.")
        elif set(TransHST).issubset(allowed_char) == False:
            print("Data Entry Error - Transaction hit contains invalid characters.")
        else:
            break

    while True:
        allowed_char = set("1234567890.")
        TransTotal = input("Enter the transaction total: ")
        if TransTotal == "":
            print("Data Entry Error - Transaction total cannot be blank.")
        elif set(TransTotal).issubset(allowed_char) == False:
            print("Data Entry Error - Transaction total contains invalid characters.")
        else:
            break

    # save inputs to data file
    y = open("TransactionInfo.dat", "a")
    y.write("{}, ".format(str(TransID)))
    y.write("{}, ".format(DrivNum))
    y.write("{}, ".format(TransDate))
    y.write("{}, ".format(TransDesc))
    y.write("{}, ".format(TransAmount))
    y.write("{}, ".format(TransHST))
    y.write("{}, ".format(TransTotal))
    y.close()
print()
print("Data Saved")
#run function and ask if want to run it again
transaction_input()
while True:
    allowed_char = set("YNyn")
    RunAgain = input("Would you like to enter another driver's information(Y/N)?: ").upper()
    print()
    if RunAgain =="":
        print("Data Entry Error - Cannot be blank")
    elif set(RunAgain).issubset(allowed_char) == False:
        print("Data Entry Error - Must enter Y or N")
    elif RunAgain == "Y":
        transaction_input()
    else:
        break
