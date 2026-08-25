try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print("Result =", a / b)

except ValueError:
    print("Enter only numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")
