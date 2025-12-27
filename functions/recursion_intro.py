"""
Problem:
Demonstrate a simple recursive function in Python.

Approach:
- Define a function that calls itself
- Show how recursion works for small problems
- Use base case to prevent infinite recursion

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Using the function
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")
