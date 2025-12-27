"""
Problem:
Check if a given integer number is a palindrome.

Approach:
- Reverse the number using modulo (%) and division
- Compare the reversed number with the original
- Print the result

Time Complexity:
O(d) where d is the number of digits
Space Complexity:
O(1)
"""

num = int(input("Enter an integer: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
