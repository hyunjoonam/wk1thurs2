# Exercise 2: String Interpolation
# Write an app which separatly takes first name and last name of the user. Once the name is taken print out the following message: 

# Hello, My name is FirstName, LastName

firstName = raw_input("What is your first name?")
lastName = raw_input("What is your last name?")
sentence = "Hello, My name is %s, %s" % (firstName, lastName)
print sentence