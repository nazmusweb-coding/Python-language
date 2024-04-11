# Nested while loops

# Example
final_score = 0
counter = 0

while counter < 10:
  current_number = input('Please provide a number to add: ')
  while not current_number.isnumeric():
    current_number = input('That\'s not a number! Try again: ')
  final_score += int(current_number)
  counter += 1

print('The score is', final_score)

# Exercise

n_numbers = int(input("How many numbers will be given? "))
sum = 0
i = 0

while i < n_numbers:
  user_input = input("Provide a number: ")
  while not user_input.isnumeric():
    user_input = input("Wrong! That's not a number! Try again: ")
  i += 1
  sum += int(user_input)
  
print(sum/n_numbers)
