from turtle import Turtle

"""
-> begin_fill()
-> circle()
-> end_fill()
"""

drawer = Turtle()
drawer.color('green')
# Called just before drawing a shape to be filled:
drawer.begin_fill()
# Draw a circle with given radius:
drawer.circle(60)
# Fill the shape drawn after the call begin_fill():
drawer.end_fill()
drawer.screen.mainloop()
