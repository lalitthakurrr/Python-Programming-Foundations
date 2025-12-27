"""
Problem:
Demonstrate functions with parameters and return values in Python.

Approach:
- Define functions that accept multiple parameters
- Return a computed value
- Show clarity and modularity in code

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

# Function to calculate area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Using the functions
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

area = rectangle_area(l, w)
perimeter = rectangle_perimeter(l, w)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
