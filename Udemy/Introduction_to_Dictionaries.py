# Welcome to Dictionaries!

students = ['bob', 12, 'rachel', 13, 'emily', 15] # well its a valid approach, but in this case dictionaries are best
print(students)

students = {'bob' : 12, 'rachel' : 13, 'emily': 15}
print(students)
print(students['bob'])      # accessing values
students['rachel'] = 14     # updating values
del students['emily']       # deleting values
print(students)

# Adding values

students["me"] = 20
students.update({"you" : 22})
print(students)

# remember they key needs to be unique or different, if they are same the last key will get priotized

# syntax
# dictionary = {key : value, key : value}
