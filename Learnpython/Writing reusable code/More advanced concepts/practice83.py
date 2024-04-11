# Documenting functions

# Example
def calculate_price(weight, price_per_pound=1.5, tax=0.15):
  """Calculate price for a amount
  
  Keyword arguments:
  weight -- weight expressed in pounds
  price_per_pound -- price paid per one pound
  tax -- the tax value that needs to the price
  """
  return  weight * price_per_pound * (1+tax)

# In Python, anything put between """ and """ will be treated as a documentation string for a given function. Note where we placed the documentation: it comes right after the line beginning with def function_name, and is indented together with the function body.
# Documentation strings (or docstrings) are a convenient way to provide documentation for a function: what it does, what parameters it expects, etc.


# To know best practices related to writing function documentation in Python, read this: https://peps.python.org/pep-0257/
