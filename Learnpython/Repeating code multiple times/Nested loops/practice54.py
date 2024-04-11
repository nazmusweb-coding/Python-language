# Nested for loops – explanation

for i in range(1, 10):
    for j in range(1, 2):
        print(str(i) + str(i) + str(i) + str(i) + str(i) + str(i) + str(i) + str(i) + str(i))

# Another code

line_to_print = ''
for i in range(1, 10):
    for j in range(1, 10):
        line_to_print += str(i)
    print(line_to_print)
    line_to_print = ''