from turtle import Turtle

drawer = Turtle()
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        drawer.color(c)
        drawer.forward(steps)
        drawer.right(30)

drawer.screen.mainloop()
