# Exercise 3: Tip Calculator
# In this assignment you are going to ask the user for the two inputs as shown below:

# - Enter the total amount

# - Enter the tip percentage amount

# After the user has entered both inputs the application calculates the tip amount and displays it to the user.

totalAmount = int(raw_input("Enter the total amount $"))
tipPercentage = int(raw_input("Enter the tip percentage %"))

tipAmount = totalAmount*tipPercentage*0.01
sentence = "The tip amount is $%d" % tipAmount

print sentence