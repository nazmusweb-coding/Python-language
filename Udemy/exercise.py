# generating factorial
def calculate_factorial(number):
    fac = 1
    for i in range(1, number+1):
        fac *= i
    return fac

print(calculate_factorial(5)) 