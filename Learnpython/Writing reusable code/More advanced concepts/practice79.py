# None – explanation, None is almost same as NULL in other programming languages

# Example
def safe_division(x, y):
  if y == 0:
    return None
  else:
    return x/y
  
# Exercise
def safe_division(x, y):
  if y == 0:
    return None
  else:
    return x/y

print(safe_division(2, 5))
print(safe_division(2, 0))
