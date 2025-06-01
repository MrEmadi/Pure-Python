from turtle import Turtle

"""
-> backward()
-> right()
"""

drawer = Turtle()
# Send the turtle backward 100 steps:
drawer.backward(100)
for _ in range(3):
    # Change the direction of the turtle (clockwise):
    drawer.right(90)
    drawer.backward(100)

drawer.screen.mainloop()
