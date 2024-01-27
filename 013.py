# Class definition
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
 
    def bark(self):
        return "Woof!"
 
# Creating an object
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)
print(my_dog.bark())
