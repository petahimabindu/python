# Program to find the length of a string without using library functions

string = input("Enter a string: ")

length = 0

for character in string:
    length = length + 1

print("Length of the string =", length)
