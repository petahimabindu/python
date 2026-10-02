# Program to check whether a key is present in a dictionary

d = {"name": "Ravi", "age": 20, "city": "Anantapur"}

key = input("Enter the key to search: ")

if key in d:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")
