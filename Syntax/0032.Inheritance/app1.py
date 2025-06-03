# Inheritance:
# - Single: 'A -> B'
# - Multilevel: 'A -> B -> C'
# - Hierarchical: 'A -> C' and 'A -> B'
# - Multiple: 'A and B -> C'

# Example -> Hierarchical

# Parent class:
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self): # Main Method
        return "voice!"


# Child class:
class Dog(Animal):
    def speak(self):
        # Access to the Parent's Method -> super()
        parent_speak = super().speak()
        return f"{parent_speak} -> Hup Hup!"
    def wag_tail(self):
        return f"{self.name} is a special dog!"


# Child class:
class Cat(Animal):
    def speak(self): # Override
        return "Mue Mue!"


# Create objects:
dog = Dog("Chop")
cat = Cat("German Cat")
print(dog.speak())
print(cat.speak())
print(dog.wag_tail())
