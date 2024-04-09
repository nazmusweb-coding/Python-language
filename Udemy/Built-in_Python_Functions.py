# Built-in Python Functions

# absolute value
print(abs(-5))

# bool
print(bool(-199))

# dir
print(dir("hello")) # shows all possible string methods

# help - tell how the methods works
print(help("hello".upper))

# eval 'disguised as a string', executes strings of codes
sent = "print('hi')"
eval(sent)

# exec - eval, but multiple lines - need to work on this one

# str, int, float type conversion functions
print("hello" + str(100))
print(123 + int("456"))
print(float("123.45") + 0.23)
