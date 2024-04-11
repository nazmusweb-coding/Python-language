# Invoke function inside function

# Example
def contains_digits(word):
  for letter in word:
    if letter.isnumeric():
      return True
  return False

def contains_letters(word):
  for letter in word:
    if letter.isalpha():
      return True
  return False

def validate_password(password):
  if not contains_letters(password) or not contains_digits(password):
    return False
  else:
    return True
# First, we defined two functions that check whether (a) a given word contains digits and (b) a given word contains letters. Next, we used these functions inside another function that checks whether a user's password is in the proper format (i.e., whether it contains at least one letter and at least one digit).

# Exercise
def calculate_social_contribution(amount):
  if amount < 200:
    return 0
  elif amount < 1000:
    return 100
  else:
    return 200

def calculate_tax(amount):
  if amount <= 3000:
    return amount * 0.1
  else:
    return 300 + (amount-3000) * 0.2

def convert_gross_to_net(salary):
  print(f"Your salary gross: {salary}")
  print(f"Salary after social contribution: {salary-calculate_social_contribution(salary)}")
  print(f"Net salary after tax: {salary-calculate_social_contribution(salary)-calculate_tax(salary-calculate_social_contribution(salary))}")

convert_gross_to_net(5000)
