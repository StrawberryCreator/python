import turtle as t
import random as r

t.bgcolor ("black")
t.colormode (255)
t.speed (0)

def go (x, y):
    t.penup ()
    t.goto (x, y)
    t.pendown ()

def firework ():
    t.color (r.randint (0, 255), r.randint (0, 255), r.randint (0, 255), )
    s = r.randint (10, 25)
    l = r.randint (50, 100)
    for i in range (int(360/s)):
        t.forward (l)
        t.backward (l)
        t.right (s)

for i in range (r.randint (5, 15)):
    go (r.randint (-250, 250), r.randint (-250, 250))
    firework ()

t.mainloop ()