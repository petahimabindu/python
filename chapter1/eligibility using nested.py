age = int(input("Enter age: "))

if age >= 18:
    income = int(input("Enter income: "))

    if income >= 10000:
        print("Eligible")
    else:
        print("Income is insufficient")
else:
    print("Age is insufficient")
