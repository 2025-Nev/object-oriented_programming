class Man:
    def __init__(self, weight):
        self.weight = weight  # Attribute

    def eat(self):
        print(f"The man with weight {self.weight} is eating!")  # Method


class Woman:
    def __init__(self, height):
        self.height = height  # Attribute

    def walk(self):
        print(f"The woman with height {self.height} is walking!")  # Method


class Dog:
    def __init__(self, color):
        self.color = color  # Attribute

    def bark(self):
        print(f"The {self.color} dog is barking!")  # Method

man = Man(80)  # Create a 'Man' object with weight 80
woman = Woman(160)  # Create a 'Woman' object with height 160
dog = Dog('brown')  # Create a 'Dog' object with color 'brown'

man.eat()  # Call the 'eat' method
woman.walk()  # Call the 'walk' method
dog.bark()  # Call the 'bark' method

