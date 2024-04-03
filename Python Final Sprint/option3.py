# Enter company expenses
# by Brian Jackman
# 2024 04 02


# function for inputs and validations
def expenses_input():
    while True:
        allowed_char = set("1234567890")
        InvoiceNum = input("Enter the invoice number: ")
        if InvoiceNum == "":
            print("Data Entry Error - Invoice number cannot be blank.")
        elif set(InvoiceNum).issubset(allowed_char) == False:
            print("Data Entry Error - Invoice number contains invalid characters.")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890")
        DrivNum = input("Enter the driver number: ")
        if DrivNum == "":
            print("Data Entry Error - Driver number cannot be blank.")
        elif set(DrivNum).issubset(allowed_char) == False:
            print("Data Entry Error - Driver number contains invalid characters.")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890-")
        InvoiceDate = input("Enter the invoice date (YYYY-MM-DD): ")
        if InvoiceDate == "":
            print("Data Entry Error - Invoice date cannot be blank.")
        elif set(InvoiceDate).issubset(allowed_char) == False:
            print("Data Entry Error - Invoice date contains invalid characters.")
        elif len(InvoiceDate) != 10:
            print("Data Entry Error - Invoice date must be in format YYYY-MM-DD")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890")
        ItemNum = input("Enter the item number: ")
        if ItemNum == "":
            print("Data Entry Error - Item number cannot be blank.")
        elif set(ItemNum).issubset(allowed_char) == False:
            print("Data Entry Error - Item number contains invalid characters.")
        else:
            break
    print()

    while True:
        allowed_char = set(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
        ItemDesc = input("Enter the item description: ").title()
        if ItemDesc == "":
            print("Data Entry Error - Item description cannot be blank.")
        elif set(ItemDesc).issubset(allowed_char) == False:
            print("Data Entry Error - Item description contains invalid characters.")
        else:
            break
    print()

    while True:
        allowed_char = set("1234567890.")
        ItemCost = input("Enter the item cost: ")
        if ItemCost == "":
            print("Data Entry Error - Item cost cannot be blank.")
        elif set(ItemCost).issubset(allowed_char) == False:
            print("Data Entry Error - Item cost contains invalid characters.")
        else:
            break
    print()

    while True:
        ItemQty = input("Enter the item quantity: ")
        if ItemQty == "":
            print("Data Entry Error - Item quantity cannot be blank.")
        elif set(ItemQty).issubset(allowed_char) == False:
            print("Data Entry Error - Item quantity contains invalid characters.")
        else:
            break
    print()

    while True:
        ItemHST = input("Enter the item HST: ")
        if ItemHST == "":
            print("Data Entry Error - Item HST cannot be blank.")
        elif set(ItemHST).issubset(allowed_char) == False:
            print("Data Entry Error - Item HST contains invalid characters.")
        else:
            break
    print()

    while True:
        ItemTotal = input("Enter the item total: ")
        if ItemTotal == "":
            print("Data Entry Error - Item total cannot be blank.")
        elif set(ItemTotal).issubset(allowed_char) == False:
            print("Data Entry Error - Item total contains invalid characters.")
        else:
            break
    print()
# save inputs to data file
    x = open("ExpensesInfo.dat", "a")
    x.write("{}, ".format(InvoiceNum))
    x.write("{}, ".format(DrivNum))
    x.write("{}, ".format(InvoiceDate))
    x.write("{}, ".format(ItemNum))
    x.write("{}, ".format(ItemDesc))
    x.write("{}, ".format(ItemCost))
    x.write("{}, ".format(ItemQty))
    x.write("{}, ".format(ItemHST))
    x.write("{}, ".format(ItemTotal))
    x.close()


print()
print("Data Saved")
# run function and ask if want to run it again
expenses_input()
while True:
    allowed_char = set("YNyn")
    RunAgain = input(
        "Would you like to enter another driver's information(Y/N)?: ").upper()
    print()
    if RunAgain == "":
        print("Data Entry Error - Cannot be blank")
    elif set(RunAgain).issubset(allowed_char) == False:
        print("Data Entry Error - Must enter Y or N")
    elif RunAgain == "Y":
        expenses_input()
    else:
        break
