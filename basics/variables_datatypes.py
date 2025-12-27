"""
Problem:
Demonstrate variables and basic data types in Python.

Approach:
- Declare variables of different data types
- Perform basic operations
- Display type information using type()

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

# Integer
count = 10
print("Count:", count, "| Type:", type(count))

# Float
price = 99.99
print("Price:", price, "| Type:", type(price))

# String
course = "Python Programming"
print("Course:", course, "| Type:", type(course))

# Boolean
is_active = True
print("Is Active:", is_active, "| Type:", type(is_active))

# Type conversion
new_count = float(count)
print("Converted Count:", new_count, "| Type:", type(new_count))
