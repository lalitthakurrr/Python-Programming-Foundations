# Pseudocode for Basic Programs

## Reverse Number
1. Read integer num
2. reversed_num = 0
3. While num > 0:
    a. digit = num % 10
    b. reversed_num = reversed_num * 10 + digit
    c. num = num // 10
4. Print reversed_num

## Prime Check
1. Read integer num
2. If num <= 1 → Not prime
3. Else:
    a. For i = 2 to sqrt(num):
        i. If num % i == 0 → Not prime
4. If no divisor found → Prime
