import turtle as t
t.speed (0)
def star (x, y, color):
    t.color (color)
    t.penup ()
    t.goto (x, y)
    t.pendown ()
    for i in range (5):
        t.forward (100)
        t.right (144)
star (0, 0, "red")
t.hideturtle ()
t.mainloop ()