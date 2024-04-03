# Description: Program to print a report for HAB Taxi Services profit Listings.
# Author: Luke Metcalfe
# Date: April 2, 2024

# import required libraries
import datetime
import FormatValues as FV

# Define program constants
Today = datetime.datetime.now()

# Main report processing starts here

# BRIAN JANES: you need to have your program starting after your imports. The imports should be at the top of the file. The function is going to be taken from this to the main file that Dylan is making, and all your functions will be here and have access to the imports that you provide here in this file.

# First thing I noticed was pathing issue for your revenues.txt file. this needed to be in the root of the project for some reason. I encounter this earlier but I am not exactlty sure why!

# I already had the expenses.txt file from Nasser in my root so it did not error for me, because it just happened to also be there.
# For your open loops, they were not quite what you needed - You were trying to open the file as it is, BUT the first thing you were trying to do was loop over it and convert things to ints and floats - but this first line is all headers and will not be able to convert to strings. This is why I included next(f) and next(a) BEFORE the loop soo it will skip the first line and start at the data. This might need to be changed if the first line is not headers in the future.

# I shortened the logic to do conversions in 1 line as well - I just think that looks cleaner. personal preference - tell me to fuck off if you like!

# So now we are reading the files correctly and i am getting anerror for line 63 - in FDateS DateValueString = DateValue.strftime("%Y-%m-%d")
# I can see why this is happening BUT I will leave it here and we can chat about it tomorrow

def PrintCompanyProfitListing():

    # Open the data file
    with open("revenue.txt", "r") as f:
        # Skip the first line, they are headers.
        next(f)
        for RevenueRecord in f:
            # Read the record
            RevenueLst = RevenueRecord.split(",")
            TransID = RevenueLst[0].strip()
            DriverNum = RevenueLst[1].strip()
            TransDate = RevenueLst[2].strip()
            TransDescription = RevenueLst[3].strip()
            TransAmt = float(RevenueLst[4].strip())
            TransHST = float(RevenueLst[5].strip())
            TransTot = float(RevenueLst[6].strip())
    f.close()

    with open("expenses.txt", "r") as a:
        next(a)
        for ExpensesRecord in a:
            ExpensesLst = ExpensesRecord.split(",")
            InvoiceNum = ExpensesLst[0].strip()
            DriverNo = ExpensesLst[1].strip()
            InvDate = ExpensesLst[2].strip()
            ItemNum = ExpensesLst[3].strip()
            ItemDescription = ExpensesLst[4].strip()
            ItemCost = float(ExpensesLst[5].strip())
            ItemQty = int(ExpensesLst[6].strip())
            ItemSubTot = float(ExpensesLst[7].strip())
            ItemHST = float(ExpensesLst[8].strip())
            ItemTot = float(ExpensesLst[9].strip())
    a.close()

    # Perform required Calculations
    ProfitLoss = TransTot - ItemTot

    # Generate report headings
    print("HAB TAXI SERVICES")
    print(f"PROFIT LISTING REPORT")
    print(f"DATE: {FV.FDateS(Today):>10s}")
    print()
    print("TRANSACTION  DRIVER  TRANSACTION         TRANSACTION                            TRANSACTION   TRANSACTION  TRANSACTION")
    print("   ID        NUMBER     DATE             DESCRIPTION                               AMOUNT        HST          TOTAL")
    print("=======================================================================================================================")
    print("=======================================================================================================================")


    print()
    print("INVOICE   DRIVER   INVOICE     ITEM              ITEM                 ITEM        ITEM        ITEM          ITEM         ITEM")
    print("NUMBER    NUMBER    DATE      NUMBER         DESCRIPTION              COST        QTY        SUBTOTAL       HST          TOTAL")

    # Display the detail line
    print(f"{TransID:<4s}  {DriverNum:<5s}  {FV.FDateSFinalSprint(TransDate):<10s}         {TransDescription:<26s}                            {
          FV.FDollar2(TransAmt):>9s}   {FV.FDollar2(TransHST):>9s}   {FV.FDollar2(TransTot):>9s}")
    print(f"{InvoiceNum:<4s}   {DriverNo:<5s}   {FV.FDateSFinalSprint(InvDate):<10s}     {ItemNum:<5s}              {ItemDescription:<26s}                 {FV.FDollar2(ItemCost):>9s}        {ItemQty:<3d}        {FV.FDollar2(ItemSubTot):>9s}          {FV.FDollar2(ItemHST):>9s}        {FV.FDollar2(ItemTot):>9s}")
    print()
    print(f"PROFIT LOSS: {FV.FDollar2(ProfitLoss):>9s}")

    f.close()
    a.close()


PrintCompanyProfitListing()


