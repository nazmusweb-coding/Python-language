# Factrial function
def factorial(number):
  score = 1
  for i in range(1, number+1):
    score = score * i
  return score

# Draw pattern function
def draw_pattern(row=5, columns=8):
  line_to_print = ''
  for i in range(0, row):
    for j in range(0, columns):
      if i % 2 == 0:
        if j % 2 == 0: line_to_print += '-'
        else: line_to_print += '='
      else:
        if j % 2 == 0: line_to_print += '='
        else: line_to_print += '-'
    print(line_to_print)
    line_to_print = ''

# How much do i need to save per month to gather given amount in given time
def find_monthly_savings(amount, years):
  if  0 >= amount or years <= 0:
    return None
  return amount / (years * 12)
