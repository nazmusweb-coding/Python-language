# A convenient shortcut

counter = 1
counter = counter + 1 # is the same as counter += 1
counter = counter - 5 # is the same as counter -= 5
counter = counter * 2 # is the same as counter *= 2
counter = counter / 4 # is the same as counter /= 4

# Exercise

# Write a program that will print all powers of 2, beginning with 21=221=2 and ending with 1024.

target = 2
print("Here are some powers of 2!")
while target <= 1024:
  print(target)
  target *= 2
  
print("That's enough!")
