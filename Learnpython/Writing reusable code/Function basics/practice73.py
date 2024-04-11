# Functions without return values

def factorial(number):
  score = 1
  while number > 1:
    score = score * number
    number = number - 1

print(factorial(5))

# here nothing is returned, so None will be printed
