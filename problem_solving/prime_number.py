"""
Problem:
Check if a given number is prime.

Approach:
- A prime number is greater than 1 and divisible only by 1 and itself
- Check divisibility up to sqrt(n) for efficiency
- Print whether the number is prime or not

Time Complexity:
O(sqrt(n))
Space Complexity:
O(1)
"""

import math

num = int(input("Enter an integer: "))

if num <= 1:
    print(f"{num} is not prime.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")
