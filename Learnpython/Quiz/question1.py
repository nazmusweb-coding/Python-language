count_posters = int(input('How many posters will be printed? '))

def calculate_cost(count_posters):
  if count_posters >= 125:
    cost = (count_posters // 125) * 50 + count_posters * 1.25
  else:
    cost = 50 + count_posters * 1.25
  print(f"This will cost {cost} USE.")
  
calculate_cost(count_posters)