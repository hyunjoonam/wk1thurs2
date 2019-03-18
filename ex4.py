# Exercise 4: Advanced Tip Calculator
# Continuing off from your work on the first tip calculator, make a new file that will do the following:

# Take the total bill amount
# Ask for the quality of service and change the tip percentage based on the response
# good -> 20%
# fair -> 15%
# bad -> 10%
# Split the bill between any given number of people

totalBill = int(raw_input("What is the total bill amount? $"))
qualityOfService = raw_input("How was the quality of service? : good, fair, or bad")

while qualityOfService not in ("good", "fair", "bad"):
    print "Sorry please choose again"
    qualityOfService = raw_input("How was the quality of service? : good, fair, or bad")

else:
    if qualityOfService == 'good':
        billIncludingTip = (1.20*totalBill)
        
    elif qualityOfService =="fair":
        billIncludingTip = (1.15*totalBill)

    elif qualityOfService == "bad":
        billIncludingTip = (1.10*totalBill)
    
    numberOfPeople = int(raw_input("How many number of people"))
    print "Each person needs to pay $%s including tips" % (billIncludingTip/numberOfPeople)

