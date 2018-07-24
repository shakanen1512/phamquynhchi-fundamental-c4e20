height_cm = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))

height_m = height_cm/100
BMI = weight/(height_m**2)

if BMI < 16:
    print("You are severely underweight.")
elif 16 < BMI < 18.5:
    print("You are underweight.")
elif 18.5 < BMI < 25:
    print("You are normal.")
elif 25 < BMI < 30:
    print("You are overweight.")
else:
    print("You are obese")