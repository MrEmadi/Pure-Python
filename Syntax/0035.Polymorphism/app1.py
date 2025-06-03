# Polymorphism:
# -> Method Overriding
# -> Duck Typing

class Dog:
    def speak(self):
        return "Hup Hup!"

class Cat:
    def speak(self):
        return "Mue Mue!"

class Duck:
    def speak(self):
        return "Wak Wak!"

# A common method:
def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
duck = Duck()

# Use polymorphism:
print(animal_sound(dog))
print(animal_sound(cat))
print(animal_sound(duck))
