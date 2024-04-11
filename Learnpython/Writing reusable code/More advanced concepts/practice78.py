# Function invocation with parameter names

# Example
def calculate_price(weight, price_per_pound=1.5, tax=0.15):
  return weight * price_per_pound * (1+tax)

# Exercise
def calculate_cone_area(r=1, pi=3.14, h=1):
  return (1.0/3) * pi * r * r * h

calculate_cone_area(5, h=3) # one of the important things 