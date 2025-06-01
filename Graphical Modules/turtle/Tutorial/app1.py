from turtle import Turtle

"""
-> forward()
-> left()
"""

drawer = Turtle()
# Send the turtle forward 100 steps:
drawer.forward(100)
for _ in range(3):
    # Change the direction of the turtle (anti-clockwise):
    drawer.left(90)
    drawer.forward(100)

# Wait to be dismissed and will not exit until it is terminated:
drawer.screen.mainloop()
