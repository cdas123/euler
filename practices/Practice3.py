# A python3 program to calculate the largest prime factor of a number
import sys
from _operator import index

sys.set_int_max_str_digits(0)


class Solver:
    def find_largest_prime_number_of(self, n):
        list_of_divisible_numbers: list[int] = sorted([x for x in range(3, n, 2) if (n % x == 0 and n != x)])
        print(list_of_divisible_numbers)
        list_prime_numbers = []
        for i in list_of_divisible_numbers:
            for j in range(0, index(i)):
                if (list_of_divisible_numbers[j] / i == 1 and i == list_of_divisible_numbers[j]):
                    list_prime_numbers.append(list_of_divisible_numbers[j])
        print(max(list_prime_numbers))


if __name__ == '__main__':
    solver = Solver()
    solver.find_largest_prime_number_of(45)
