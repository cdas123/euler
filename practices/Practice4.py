import math

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return (a * b) // greatest_common_divisor(a, b)

def smallest_divisible_number(lower, upper):
    lcm_final = lower
    for i in range(lower, upper + 1):
        lcm_final = least_common_multiple(lcm_final, i)
    return lcm_final

result = smallest_divisible_number(1, 20)
print("The smallest positive number divisible by each of the numbers from 1 to 20 is:", result)