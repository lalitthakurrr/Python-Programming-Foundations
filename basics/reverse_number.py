"""
Problem:
Reverse a given integer number.

Approach:
- Extract digits using modulo (%)
- Build the reversed number iteratively
- Use a loop for each digit

Time Complexity:
O(d) where d is number of digits
Space Complexity:
O(1)
"""

# Input from user
num = int(input("Enter an integer: "))

reversed_num = 0
temp = num

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10

print(f"Original number: {num}")
print(f"Reversed number: {reversed_num}")
