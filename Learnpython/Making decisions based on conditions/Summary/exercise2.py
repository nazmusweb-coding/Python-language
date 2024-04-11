# John earns $10 per hour for the first 160 hours in a given month. For any additional hour, he earns $15 per hour. Write a program that accepts an integer number of hours worked in a given month and prints John's total earnings.

hours = int(input('Provide the number of hours worked in a month: '))

if hours > 160:
  total = 10 * 160
  hours = hours - 160
  total = total + 15 * hours
  print(total)
else:
  print(10*hours)
