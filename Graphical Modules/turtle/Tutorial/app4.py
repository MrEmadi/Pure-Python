from turtle import Turtle

"""
-> up()
-> down()
-> home()
-> pos()
"""

drawer = Turtle()
# The pen is up - no drawing when moving:
drawer.up()
drawer.forward(200)
# The pen is down - drawing when moving:
drawer.down()
drawer.right(90)
drawer.forward(200)
# Return the turtle's current location (x,y):
print(drawer.pos())
# Move turtle to the center of the page (0,0):
drawer.home()
drawer.screen.mainloop()
