import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def smallest_divisible_number(lower, upper):
    lcm_final = lower
    for i in range(lower, upper + 1):
        lcm_final = lcm(lcm_final, i)
    return lcm_final

result = smallest_divisible_number(1, 20)
print("The smallest positive number divisible by each of the numbers from 1 to 20 is:", result)