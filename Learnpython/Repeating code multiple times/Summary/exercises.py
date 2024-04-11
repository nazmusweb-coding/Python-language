# Use a loop to calculate and print the value of 10 factorial (10!).

factorial = 1
for i in range(1, 11):
    factorial *= i
print(factorial)

# Keep asking the user to guess a secret number until they get it right. The secret number is 8.
answer = input('Guess our secret number! ')

while True:
  if int(answer) == 8:
    print("Correct!")
    break
  else:
    if int(answer) > 8:
      print("Too big!")
    else:
      print("Too small!")
  answer = input("Guess out secret number! ")
 

# (-) hyphens and (=) signs

line = ''
for i in range(8):
  for j in range(12):
    if (i+j) % 2 == 0:
      line += "-"
    else:
      line += "="
  print(line)
  line = ''
