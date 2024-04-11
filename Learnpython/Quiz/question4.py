
def calculate_rental_cost(day=1, age=30):
    if age < 30:
      base_fare = 220
    else:
      base_fare = 100

    free_of_charge = day // 7
    day = day - free_of_charge
    return day * base_fare

print(calculate_rental_cost(1, 17))