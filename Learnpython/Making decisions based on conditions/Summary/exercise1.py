# Write a program that asks the user to provide a number and prints either odd number or even number based on the user input.

user_number = int(input('Provide a number: '))

if user_number % 2 == 0:
  print('even number')
else:
  print('odd number')