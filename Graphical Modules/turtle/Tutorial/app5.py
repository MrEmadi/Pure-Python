from turtle import Turtle

"""
-> clearscreen()
-> fillcolor()
"""

drawer = Turtle()
# Return or set the fillcolor of the turtle:
drawer.fillcolor('yellow')
drawer.forward(200)
drawer.left(90)
drawer.backward(200)
# Delete all drawings and all turtles from the TurtleScreen:
drawer.screen.clearscreen()
drawer.screen.mainloop()
