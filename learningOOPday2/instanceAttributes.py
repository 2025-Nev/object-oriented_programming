import random
class Vehicle():
    def type(self):
        self.randomValue = random.randint(1,10)

        
car = Vehicle()
car.type()
print(car.randomValue)

"""
The file OOP/P03_InstanceAttributes.py demonstrates how to use instance attributes in Python. The Vehicle class includes a method type that sets an instance attribute randomValue to a random integer between 1 and 10. An instance of Vehicle named car is created, the type method is called to set the instance attribute, and then car.randomValue is printed, showing the use of instance attributes.
"""
