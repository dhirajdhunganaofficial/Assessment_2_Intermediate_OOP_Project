#Base class
class Animal:
    def sound(self):
        return "Some sound"

#Derived class
class Dog(Animal):
    # Polymorphism because it is overriding the base method
    def sound(self):
        return "Bark"

class Cat(Animal):
    # Polymorphism because it is overriding the base method
    def sound(self):
        return "Meow"

#Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
