country_capital = {
    "Vietnam" : "Hanoi",
    "Japan" : "Tokyo",
    "Germany" : "Berlin",
    "Russia" : "Moscow",
    "Mexico" : "Mexico City",
    "Canada" : "Ottawa",
    "Egypt": "Cairo",
    "Australia" : "Canberra"
}

loop = True
count = 0

while loop: 
    for key in country_capital.keys():
        print(key, end = "\t")
    print()

    country = input("Enter your country: ")
    if country in country_capital:
        print("The capital is ", country_capital[country])
    else:
        print("Not found")
        select = input("Do you want to contribute? Y/N. ").upper()
        if select == "Y":
            capital = input("Enter the capital: ")
            country_capital[country] = capital
        if select == "N":
            print("Thank you for using our services")
            break
    count += 1
