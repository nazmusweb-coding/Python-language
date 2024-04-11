# Ask the user for integer a, b, and c and print the smallest of them.

a = int(input('a=? '))
b = int(input('b=? '))
c = int(input('c=? '))

def smallest(a, b, c):
  if b > a < c:
    print(a)
  elif a > b < c:
    print(b)
  elif b > c < a:
    print(c)
    
smallest(a, b, c)