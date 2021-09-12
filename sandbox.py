# factorial

def calc_factorial(n):
    return 1 if (n == 1 or n == 0) else n * calc_factorial(n - 1)


num = 5
calc_factorial(num)
print("Factorial of", num, "is", calc_factorial(num))
