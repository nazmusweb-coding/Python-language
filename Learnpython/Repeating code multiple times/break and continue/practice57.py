# break with for loops

# Example
# The program above asks the user to provide a nickname without digits
user_input = input('Please provide a nickname for yourself. Don\'t use digits! ')
is_valid = True
for character in user_input:
  if character.isdigit():
    is_valid = False 
    break

if is_valid == True:
  print('Nickname correct!')
else:
  print('Nickname incorrect!')

# Exercise

user_number = int(input('Please provide a number from 2 to 1000: '))

flag = True

if 2 <= user_number <= 1000:
  for i in range(2, user_number):
    if user_number % i == 0:
      flag = False
  if flag == True:
    print(f"{user_number} is prime!")
  else:
    print(f"{user_number} is not prime!")
else:
  print("Incorrect number!")
