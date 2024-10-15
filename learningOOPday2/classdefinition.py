class MyFirstClass():
    #Class Attributes
    var = 10

firstObject = MyFirstClass()
print(firstObject)      #Printing object's memory hex
print(firstObject.var)  #Accessing Class Attributes

secondObject = MyFirstClass()
print(secondObject)
print(secondObject.var)

#The file OOP/P01_ClassDefinition.py contains a simple Python program demonstrating how to define a class, create class attributes, and instantiate objects
#The class MyFirstClass has a class attribute var set to 10. The program then creates two objects of this class and prints their memory addresses as well as the value of the class attribute var for each object.
