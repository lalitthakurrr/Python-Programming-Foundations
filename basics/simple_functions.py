"""
Problem:
Demonstrate creation and usage of simple functions in Python.

Approach:
- Define a function that takes input parameters
- Perform a simple calculation
- Return the result and display it
- Show modular, reusable code

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

# Function to greet a user
def greet(name):
    return f"Hello, {name}!"

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Using the functions
user_name = input("Enter your name: ")
print(greet(user_name))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", add_numbers(x, y))
