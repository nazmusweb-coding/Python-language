# Placeholders in strings

name = "jake"
sentence = "%s is 15 years old" # single placeholder

print(name + " is 15 years old")
print(sentence % name)

sentence = "%s %s was the president of the US" # multiple placeholders

print(sentence % ("Barack", "Obama"))

# Placeholders in integers

sentence = "%s is %d years old"

print(sentence % ("Sakib", 20))

# format strings (prefix f/F"{}")

name = "Sakib"

print(F"Hello, {name}") # exampole of string

x = 10
y = 20

print(f"The sum of x and y is {x+y}") # example of integer
