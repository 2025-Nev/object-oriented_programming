class Vehicle():
    #Class Methods/ Attributes

    #Here self is passed as an argument because instance is passed as first argument
    def type(self):     #Without self it throws an error
        print(self)
        print('I have a type')

car = Vehicle()
print(car)
car.type()

#A class Vehicle is defined with an instance method type.
#The type method prints the instance (self) and a message.
#An instance car of Vehicle is created.
#The instance method type is called on car, printing the instance and the message.
