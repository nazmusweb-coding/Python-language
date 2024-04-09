# If statements – multiple conditions with or

has_credit_card = input('Do you have a credit card [y/n]? ')
has_debit_card = input('Do you have a debit card [y/n]?')

if (has_credit_card == 'y' or has_debit_card == 'y'):
  print('We are happy to accept your payment.')
else:
  print('Sorry, we cannot accept your payment.')

# Exercise

weight = float(input('What is your weight in kg? '))
height = float(input('What is your height in centimeters? '))

if height < 130 or weight < 45:
  print('You can take a ride!')
else:
  print('Sorry, you cannot take a ride!')
