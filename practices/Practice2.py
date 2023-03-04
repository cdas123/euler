# A python3 program to calculate sum of the even-valued fibonacci terms not exceeding four million
import sys;

sys.set_int_max_str_digits(0)


def sumOfEvenValuedFibonacciTerms(list):
    sum = 0;
    for i in list:
        if (i % 2 == 0):
            sum = sum + i;
    print(sum);


class Solver:
    def fibonacciSeries(self, n):

        if (n > 4000000):
            sys.exit("Cancelling the calculation as the number exceeds four million")
        listOfFibonacciNumbers: list[int] = [i for i in range(0, n) if i <= 1]
        for i in range(2, n):
            listOfFibonacciNumbers.append(listOfFibonacciNumbers[i - 1] + listOfFibonacciNumbers[i - 2])
            i = i + 1
        sumOfEvenValuedFibonacciTerms(listOfFibonacciNumbers);


if __name__ == '__main__':
    number = int(input("enter number\n"))
    solver = Solver();
    solver.fibonacciSeries(number);
