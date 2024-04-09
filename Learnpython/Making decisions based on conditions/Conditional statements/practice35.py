# Nested if statements

has_middle_name = input('Do you have a middle name? Answer y or n: ')
if has_middle_name == 'y':
  likes_middle_name = input('And do you like your middle name? Answer y or n: ')
  if likes_middle_name == 'y':
    print('That is good!')
  elif likes_middle_name == 'n':
    print('Sorry to hear that.')
  else:
    print('I do not understand your answer.')
elif has_middle_name == 'n':
  print('Aw, never mind.')
else:
  print('I do not understand your answer.')

# Exercise

year = int(input('Provide a year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print('leap year')
else:
  print('not a leap year')