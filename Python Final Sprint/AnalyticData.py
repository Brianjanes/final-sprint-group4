# Analytics Data: Final Sprint.
# Morgan Browne

# Function to generate analytics data
def generateAnalyticsData():
    # Load data from text files
    employees = []
    with open('employees.txt', 'r') as empFile:
        for line in empFile:
            employeeData = line.strip().split(',')
            employees.append({
                'driverNumber': employeeData[0],
                'nameFirst': employeeData[1],
                'carID': employeeData[2],
                'balanceDue': float(employeeData[3])
            })

    revenues = []
    with open('revenue.txt', 'r') as revFile:
        for line in revFile:
            revenueData = line.strip().split(',')
            revenues.append({
                'transactionID': revenueData[0],
                'date': revenueData[3],
                'description': revenueData[4],
                'amount': float(revenueData[5]),
                'tax': float(revenueData[6]),
                'total': float(revenueData[7])
            })

    expenses = []
    with open('expenses.txt', 'r') as expFile:
        for line in expFile:
            expenseData = line.strip().split(',')
            expenses.append({
                'invoiceNumber': expenseData[0],
                'date': expenseData[3],
                'description': expenseData[5],
                'subTotal': float(expenseData[3])
            })

    print(expenses)
    print(revenues)
    print(employees)

    # Calculate total revenue
    totalRevenue = sum(float(row[4]) for row in revenues)

    # Calculate average revenue per transaction
    averagRevenuePerTransaction = totalRevenue / len(revenues)

    # Calculate total expenses
    totalExpenses = sum(float(row[2]) for row in expenses)

    # Calculate total number of employees
    totalEmployees = len(employees)

    # Calculate average expense per employee
    if totalEmployees > 0:
        averageExpensePerEmployee = totalExpenses / totalEmployees
    else:
        averageExpensePerEmployee = 0

    # Print analytics data
    print("Analytics Data:")
    print("Total Revenue: ${:.2f}".format(totalRevenue))
    print("Average Revenue per Transaction: ${:.2f}".format(
        averagRevenuePerTransaction))
    print("Total Expenses: ${:.2f}".format(totalExpenses))
    print("Total Number of Employees: {}".format(totalEmployees))
    print("Average Expense per Employee: ${:.2f}".format(
        averageExpensePerEmployee))

    # Calculate total revenue for each driver
    driverPayment = {}
    for row in revenues:
        driverNumber = row[0]
        paymentAmount = float(row[4])
        if driverNumber in driverPayment:
            driverPayment[driverNumber] += paymentAmount
        else:
            driverPayment[driverNumber] = paymentAmount

    # Calculate bonus eligibility
    bonusEligibleDrivers = []
    for employee in employees:
        driverNumber = employee[0]
        # $1,000 bounus can be changed.
        if driverNumber in driverPayment and driverPayment[driverNumber] >= 1000:
            # Append tuple of driver number and name
            bonusEligibleDrivers.append((driverNumber, employee[1]))

    # Print bonus eligibility
    print("Drivers Eligible for Bonus:")
    if bonusEligibleDrivers:
        for driver in bonusEligibleDrivers:
            print("Driver ID: {}, Name: {}".format(driver[0], driver[1]))
    else:
        print("No drivers are eligible for a bonus at this time.")

generateAnalyticsData()