print ("Please enter your login ID and password: ")
login = input("Login ID: ")
if login != "shakanen":
    print ("Please try again")
else:
    password = input("Password: ")
    if password != "willer":
        print ("Please try again")
    else:
        print ("Welcome,", login)
