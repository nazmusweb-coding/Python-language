# If statements – multiple conditions with not  (negation)

user_input = input('Please enter a number: ')
if (not user_input.isnumeric()):
  print('This is not a number!')
else:
  print('This is a correct number!')

# Exercise

password = input('Please provide a password: ')


if len(password) >= 8 and not password.startswith('@'):
  print('Correct password!')
else:
  print('Incorrect password!')


# Leaned new functions
# 1. len(string)
# 2. string.startswith('x')
