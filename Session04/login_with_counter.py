loop = True
count = 0

while loop:
    print ("Please enter your login ID and password: ")
    login = input("Login ID: ")
    if login != "shakanen":
        print ("User not found")
    else:
        password = input("Password: ")
        if password != "willer":
            print ("Password is incorrect")
        else:
            print ("Welcome,", login)
            break
    count += 1
    if count == 5:
        print("You have failed to log in 5 times.")
        print("Please contact administrator")
        loop = False
