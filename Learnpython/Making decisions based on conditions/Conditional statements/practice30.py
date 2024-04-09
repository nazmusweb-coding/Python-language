# If statements – multiple lines of code

answer1 = input('How many centimeters are there in a meter?')
if int(answer1) == 100:
  print('Very good!')
  print('Thank you!')
else:
  print('Not really...')
  print('Try harder!')

# Exercise

answer = input('Welcome, are you a registered user? y/n: ')

if answer == 'y':
  username = input('Please provide your username: ')
  print('Welcome back,', username,'!')
else:
  print('Sorry, the system does not accept new user')
