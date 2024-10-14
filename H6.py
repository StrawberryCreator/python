import turtle as t
import random as r

t.speed (0)
t.bgcolor ("dark blue")
t.colormode (255)

def randColor ():
    t.color (r.randint(55, 255), r.randint(55,255), r.randint(55,255))

def randPos (x, xx, y, yy):
    t.penup ()
    t.goto (r.randint (x, xx), r.randint(y, yy))
    t.pendown ()

def randDirect ():
    t.setheading (r.randint(0, 359))

def star (s):
    t.penup ()
    t.pendown ()
    for i in range (5):
        t.forward (s)
        t.right (144)
    
def randStar ():
    randColor ()
    randPos (-350, 325, -300, 300)
    randDirect ()
    star (r.randint(1, 25))

def moon ():
    t.color ("white")
    t.begin_fill ()
    t.circle (25)
    t.end_fill ()
    t.forward (10)
    t.color ("dark blue", "darkblue")
    t.begin_fill ()
    t.circle (25)
    t.end_fill ()

moon ()
for i in range (50):
    randStar ()



t.mainloop ()