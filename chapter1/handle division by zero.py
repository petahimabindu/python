try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")
