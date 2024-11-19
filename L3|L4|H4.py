import turtle as t
import random as r

t.hideturtle ()
t.speed (0)
t.bgcolor ("light blue")
t.color ("yellow")

t.begin_fill ()
t.goto (-250, 100)
t.goto (250, 100)
t.goto (250, -200)
t.goto (-250, -200)
t.goto (-250, 100)
t.end_fill ()

def sand ():
    t.color ("orange")
    t.penup ()
    t.goto (r.randint(-245, 245), r.randint(-195, 95))
    t.pendown ()
    t.begin_fill ()
    t.circle (1)
    t.end_fill ()

for x in range (100):
    sand ()

t.mainloop ()