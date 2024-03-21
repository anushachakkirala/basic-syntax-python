# Example Python program demonstrating datatypes, variables, loops, and functions

# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input: Get a positive integer from the user
try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        raise ValueError("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Calculate and print the factorial of the input number
print(f"Factorial of {num} is {factorial(num)}")

# Example of using variables
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Example of using loops
for i in range(5):
    print(f"Loop iteration {i+1}")

# Example of using datatypes
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "Alice", "age": 25}
my_set = {1, 2, 3}

print(f"My list: {my_list}")
print(f"My dictionary: {my_dict}")
print(f"My set: {my_set}")
