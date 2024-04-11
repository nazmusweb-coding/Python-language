# for loop with strings

# Example
secret_message = 'hello from the other side'
e_count = 0

for letter in secret_message:
  if letter == 'e': 
    e_count = e_count + 1 
print(e_count)

# Exercise
user_input = input('Please provide a password: ')

digit_count = 0
for i in user_input:
  if i.isnumeric():
    digit_count+=1

print(f"Your password contains {digit_count} digits")
