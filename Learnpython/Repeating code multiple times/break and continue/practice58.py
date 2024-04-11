# continue with while loops

# Example
counter = 0
while counter < 10:
  counter += 1
  if counter == 3: 
    continue
  print('Current value:', counter)

# Exercise
current_value = 0
while current_value < 100:
  current_value += 2
  if current_value % 6 == 0:
    continue
  print(current_value)
print('That\'s enough!')
