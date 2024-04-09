# Introduction to Tuples
# Tuples are immutable - they can't be modified
# Use case: Constancy and safety

tup = ("oranges", "apples", "bananas")
print(tup)

# Accessing and slicing
print(tup[0])       
print(tup[0:2])

# Concatenate
tup2 = (12, 14)

tup3 = tup + tup2
print(tup3)
