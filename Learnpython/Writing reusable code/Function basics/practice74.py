# Create a function called find_divisors that takes an integer x and prints its divisors from 2 to x-1, each on a new line.

def find_divisors(x):
  for i in range(2, x):
    if x % i == 0:
      print(i)
      
find_divisors(20)

