# while loops for user input

# Example
user_input = input('Please provide a number: ')
while not user_input.isnumeric():
  user_input = input('Not a number! Please provide a number: ')
print('Your number is:', user_input)

# Exercise

secret_number = 7
user_input = int(input('Guess the secret number (0-9): '))
while not user_input == secret_number:
  user_input = int(input("Wrong! Try again (0-9):" ))
print("Correct!")
