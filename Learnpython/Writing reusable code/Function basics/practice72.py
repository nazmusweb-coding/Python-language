# Using a function return value

# Example
def factorial(number):
  score = 1
  while number > 1:
    score = score * number
    number = number - 1
  return score

result = factorial(5)

# Exercise
def factorial(number):
  score = 1
  while number > 1:
    score = score * number
    number = number - 1
  return score

a = factorial(3)
b = factorial(4)
print(a+b)

