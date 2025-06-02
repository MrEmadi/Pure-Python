from turtle import Turtle

"""
-> shape()
"""

drawer = Turtle()
# Set turtle shape to shape with given name or return current shape name:
print(drawer.shape())
drawer.shape('turtle')
drawer.forward(100)
for _ in range(3):
    drawer.left(90)
    drawer.forward(100)

drawer.screen.mainloop()
