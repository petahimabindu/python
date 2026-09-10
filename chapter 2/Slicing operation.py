# Program to perform slicing on a list

numbers = [10, 20, 30, 40, 50, 60, 70]

print("Original List:", numbers)

# Slice from index 1 to 4
print("numbers[1:5]:", numbers[1:5])

# Slice from beginning to index 3
print("numbers[:4]:", numbers[:4])

# Slice from index 3 to end
print("numbers[3:]:", numbers[3:])

# Slice with step
print("numbers[::2]:", numbers[::2])

# Reverse the list using slicing
print("Reversed List:", numbers[::-1])
