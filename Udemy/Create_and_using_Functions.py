# Welcome to Functions!

# A baker makes special bread
# Series of steps: mix, knead, rise, bake

# make_special_bread() performs these  steps

# def keyword indicates starting of function

def hello_world():
    print("Hello World!")

hello_world()

def greeting(name):
    print("Hi " + name + "!")

greeting("Sakib")

def add(num1, num2):
    print(num1 + num2)

add(10, 15)

# returning; marks the ending of a function
def product(num1, num2):
    return num1 * num2
num_product = product(10, 20)
print(num_product)


def add(a, b):
    return a + b

print(product(add(1, 2) , add(3, 4)))