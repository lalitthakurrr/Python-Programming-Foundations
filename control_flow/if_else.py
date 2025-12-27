"""
Problem:
Demonstrate conditional execution using if, elif, and else.

Approach:
- Take an integer input
- Check multiple conditions
- Print appropriate output based on logic

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
