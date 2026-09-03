# Program to define a function using default arguments

def greet(name, message="Welcome to Python"):
    print(name, "-", message)

name = input("Enter your name: ")

greet(name)
greet(name, "Good Morning")
