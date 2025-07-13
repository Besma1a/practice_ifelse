firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

if firstName and lastName:
    print("Welcome " + firstName + " " + lastName + "!")
else:
    print("Error: Both first name and last name must be provided.")

username = input ("please enter your username: ")
password = input ("please enter your password: " )

if username == "admin" and password == "password123":
    print ("login successful")
elif username != "admin":
    print ("error! invalid username" )
else:
    print ("invalid password")