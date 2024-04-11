# break with while loops

# Example
user_input = input('Please provide a number: ')
while True:
  if user_input.isnumeric():
    break
  user_input = input('Not a number! Please provide a number: ')
print('Your number is:', user_input)


# Exercise
year = input('In which year was Python first released? ')

while True:
  if int(year) == 1990:
    break
  year = input("In which year was Python first released? ")
print("Correct!")