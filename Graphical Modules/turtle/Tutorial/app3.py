from turtle import Turtle
from math import sqrt

"""
-> color()
-> width()
"""

drawer = Turtle()
# Change the color of lines:
drawer.color('blue')
# Change the width of lines:
drawer.width(4)
a = 130
b = 140
drawer.forward(a)
drawer.left(135)
drawer.forward(sqrt(a ** 2 + b ** 2))
drawer.left(135)
drawer.forward(b)
drawer.screen.mainloop()
