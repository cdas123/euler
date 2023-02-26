# A python3 program to calculate sum of multiples of 3 and 5 below 1000.

class Calculator:
    def sumOfMultiplesOf3And5(self, n):
        res = 0;
        for i in range(1, n):
            if (i % 3 == 0 or i % 5 == 0):
                res = res + i;
                i = i + 1;
        return res;


if __name__ == '__main__':
    solver = Calculator()
    print(solver.sumOfMultiplesOf3And5(1000));
