# Printing average value

count_numbers = int(input('How many numbers do you have? '))

sum = 0
for i in range(0, count_numbers):
  number = int(input('Provide a number: '))
  sum += number
print(f"The average is {sum/count_numbers}")
