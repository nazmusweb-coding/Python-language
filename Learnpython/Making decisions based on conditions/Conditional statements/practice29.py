# If statements – comparison operators

# less than: <,
# greater than: >,
# less than or equal: <=,
# greater than or equal to: >=,
# equals: ==,
# not equal to: !=.

password = input('Provide the password! ')
if password != 'sEcrEt':
  print('You shall not pass!')

# Exercise

answer = int(input('How old are you? '))

if answer >= 17:
  print('You can already drive a car in England')
else:
  print('You cannot already drive a car in England yet')
  
if answer >= 18:
  print('You can already drive a car in Portugal')
else:
  print('You cannot drive a car in Portugal yet')