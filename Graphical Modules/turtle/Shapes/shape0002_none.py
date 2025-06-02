from turtle import Turtle

drawer = Turtle()
while True:
    drawer.forward(200)
    drawer.left(170)
    # 'abs(pos()) < 1' is a good way to know when the turtle is back at its home position:
    if abs(drawer.pos()) < 1:
        break

drawer.screen.mainloop()
