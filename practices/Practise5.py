def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    return sum(range(1, n+1))**2

number = 10
difference = square_of_sum(number) - sum_of_squares(number)
print("The difference = ", difference)