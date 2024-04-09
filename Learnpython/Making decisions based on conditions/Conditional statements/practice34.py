# If statements – joining even more conditions

driver_nationality = input('What is your nationality? ')
driver_age = int(input('What is your age? '))
if (driver_nationality == 'Spanish' 
  or driver_nationality != 'Spanish' and driver_age >= 26):
  print('You are good to go!')
else:
  print('Sorry, no car for you!')

# Priority list 
# Python checks all conditions in the following order: not, and, or.

purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')

if purchase_days_ago <= 14 and is_used == 'n' or is_broken == 'y':
  print('Refund')
else:
  print('No refund')

  