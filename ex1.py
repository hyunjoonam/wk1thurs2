# Exercise 1: Add Two Numbers
# Create an app which takes two numbers as input from the user and then prints out the results of addition on the screen


num1 = int(raw_input("What is your favorite number?"))
num2 = int(raw_input("What is your least favorite number?"))
add = num1 + num2
sentence = "%s plus %s is %s" % (num1, num2, add)

print sentence