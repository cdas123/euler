# A python3 program to calculate sum of the even-valued fibonacci terms not exceeding four million
import sys

sys.set_int_max_str_digits(0)


def sum_of_even_valued_fibonacci_terms(list_of_fibonacci_numbers):
    sum_of_even_numbers = sum(list(filter(lambda x: x % 2 == 0, list_of_fibonacci_numbers)))
    print(sum_of_even_numbers)



class Solver:
    def fibonacci_series(self, n):

        if (n > 4000000):
            sys.exit("Cancelling the calculation as the number exceeds four million")
        list_of_fibonacci_numbers: list[int] = [i for i in range(0, n) if i <= 1]
        for i in range(2, n):
            list_of_fibonacci_numbers.append(list_of_fibonacci_numbers[i - 1] + list_of_fibonacci_numbers[i - 2])
            i = i + 1
        sum_of_even_valued_fibonacci_terms(list_of_fibonacci_numbers);


if __name__ == '__main__':
    number = int(input("enter number\n"))
    solver = Solver()
    solver.fibonacci_series(number)
