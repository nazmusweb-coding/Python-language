# OOP - Class Inheritance

# Base model - engine, wheels, etc.
# Sports  model - powerful engine..

class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 5

    def drive(self):
        print("Driving a car....")

myCar = Car()
myCar.drive()

class SportsCar(Car): # inherit, # we can overwrite the values and functions of parent class, or it will stay default value or funtion of parent class
    def __init__(self):
        # Remember this executes the init function of the parent class
        self.engine_power = "400 HP"
        self.seats = 2

    def drive(self):
        print("Drive a sports car....")

mySportsCar = SportsCar()
mySportsCar.drive()
