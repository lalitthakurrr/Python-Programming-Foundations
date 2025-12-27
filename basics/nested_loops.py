"""
Problem:
Demonstrate nested loops in Python.

Approach:
- Use a nested for loop to print a pattern
- Illustrate how the number of operations grows with input
- Show clear separation between outer and inner loops

Time Complexity:
O(n^2)

Space Complexity:
O(1)
"""

n = 5

print("Nested loop pattern:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
