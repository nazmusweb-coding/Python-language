# Functions with multiple parameters

# Example
def print_between(lower, upper):
  for i in range (lower, upper+1):
    print('Current value:', i)

# Exercise
def convert(amount, rate):
  print(f"Amount: {amount} Rate: {rate} Conversion: {amount*rate}")

convert(55, 1.75)