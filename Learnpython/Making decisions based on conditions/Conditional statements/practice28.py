# If statements – elif

john_age = 25
user_input = input('How old are you?')
user_age = int(user_input)

if user_age > john_age:
  print('You are older than John.')
elif user_age == john_age:
  print('You are as old as John.')
else:
  print('You are younger than John.')

# Exercise
answer = input('Is Sydney the capital of Australia? ')

if answer == 'y':
  print('Wrong! Canberra is the capital!')
elif answer == 'n':
  print('Correct!')
else:
  print('I do not understand your answer!')
    