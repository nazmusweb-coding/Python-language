# Mandatory and optional arguments together

# Example
def calculate_price(weight, price_per_pound=1.5, tax=0.15):
  return weight * price_per_pound * (1+tax)

# Exercise
def calculate_area(r, pi=3.14):
  return pi * r * r
