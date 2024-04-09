# Introduction to For loops

list1 = ['apples', 'bananas', 'cherries']
tup1 = (2, 6, 7)

# Notice the identation
for item in tup1:
    print(item)

# range
for i in range(1, 11):
    print(i)

# Even; 2 here is the increment factor
for i in range(2, 11, 2):
    print(i)

# First 10 multiples of 5
for i in range(5, 51, 5):
    print(i)

# Nested for loop
for i in range(1, 6):
    for j in range(1, 3):
        print(i * j)
