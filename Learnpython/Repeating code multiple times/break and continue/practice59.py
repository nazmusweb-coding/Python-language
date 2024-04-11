# continue with for loops

# Example
for i in range(1, 11):
  if i % 2 != 0:
    continue
  print(i) 

# Exercise

for i in range(0, 15):
  i += 1
  remainder = i % 5
  if remainder == 0:
    continue
  print(f"The remainder of dividing {i} by 5 is {remainder}")