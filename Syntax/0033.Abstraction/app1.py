from abc import ABC, abstractmethod


# Define an abstract class:
class Shape(ABC):

    @abstractmethod
    def area(self): # abstract method
        pass # without body


# Child classes:
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # abstract method (body):
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # abstract method (body):
    def area(self):
        return 3.14 * self.radius ** 2


rect = Rectangle(5, 4)
print("Rectangle:", rect.area())
circle = Circle(3)
print("Circle:", circle.area())
