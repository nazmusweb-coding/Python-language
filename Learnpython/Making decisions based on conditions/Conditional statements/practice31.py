# If statements – multiple conditions with and

# Perfect. Sometimes, more than one condition needs to be met in order to execute a part of code. To that end, we can use Boolean operators. The first operator we'll look at is and:

nationality = input('What is your nationality? ')
age = input('What is your age? ')

if (nationality == 'German' and int(age) > 25):
  print('You are eligible to apply.')
else:
  print('Sorry, only German citizens above 25 can apply.')

# Exercise

name = input('Provide a Polish name: ')

if name == 'Kuba':
  print('This is a male name')
elif name.endswith('a'):
  print('This is a female name')
else:
  print('This is a male name')

# Learned new function name.endwith('a')