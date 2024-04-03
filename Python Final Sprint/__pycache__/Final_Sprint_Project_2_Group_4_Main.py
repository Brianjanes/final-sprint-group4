# Description: Main body for a program for HAB Taxi Services to handle employees, finances, and car rentals
# Author: Dylan Haire
# Date(s): Apr. 01, 2024; Apr. 02, 2024

# Import libraries
import datetime

# Define program constants.
curDate = datetime.datetime.now()
# Read values from Defaults.dat and assign them to variables
f = open("Defaults.dat", "r")
numNextTrans = int(f.readline())
numNextDriver = int(f.readline())
feeMnthStand = float(f.readline())
feeRentDay = float(f.readline())
feeRentWeek = float(f.readline())
RATE_HST = float(f.readline())

# Print values to the screen to verify that they have been read correctly
print(numNextTrans)
print(numNextDriver)
print(feeMnthStand)
print(feeRentDay)
print(feeRentWeek)
print(RATE_HST)

# Define program functions.
	# Option 1:
	
	# Option 2:
	
	# Option 3: 
	
	# Option 4:
	
	# Option 5: 
	
	# Option 6: 
	
	# Option 7: 
	
	# Option 8: 
	
# Main program.
while True:
	# Method 1:
    # Store the current date as a constant at program startup
    # Save the current date to Defaults.dat each time the program runs
    # Compare the current date to the previous date stored in Defaults.dat
    # If the month has incremented, charge the monthly stand fees, notify the user, and write the data to Revenue.txt
    # Segment this portion so that it runs independently of the main program
	print("Current date: ", curDate)
	print()
    # Gather user input.
		# Get an input from the user indicating their program choice (Validation - Must be 1-9)
	choiceProg = input("Enter the desired program (1-9): ")
	choiceProg = int(choiceProg)
	
    # Perform required calculations
    # Select the function to run based on the user's input
	if choiceProg == 1:
		print("Option 1 Selected")
	elif choiceProg == 2:
		print("Option 2 Selected")
	elif choiceProg == 3:
		print("Option 3 Selected")
	elif choiceProg == 4:
		print("Option 4 Selected")
	elif choiceProg == 5:
		print("Option 5 Selected")
	elif choiceProg == 6:
		print("Option 6 Selected")
	elif choiceProg == 7:
		print("Option 7 Selected")
	elif choiceProg == 8:
		print("Option 8 Selected")
	else:
		print("Quitting program...")
		break
    # Display results
	break
# Any housekeeping duties at the end of the program.
