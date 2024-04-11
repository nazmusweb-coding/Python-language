# Functions with return values

# Example
def factorial(number):
  score = 1
  while number > 1:
    score = score * number
    number = number - 1
  return score

# Exercise
# Write a function named return_bigger(a, b) that takes two numbers and returns the bigger one. If the numbers are equal, return 0.
def return_bigger(a, b):
  if a > b: return a
  elif a < b: return b
  else: return 0
