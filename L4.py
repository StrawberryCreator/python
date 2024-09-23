import turtle as t
t.speed (0)

#functions

def goto (x, y):
    t.penup ()
    t.goto (x, y)
    t.pendown ()

def rec (l, h, c):
    t.color (c)
    t.begin_fill ()
    for i in range (2):
        t.forward (l)
        t.left (90)
        t.forward (h)
        t.left (90)
    t.end_fill ()

def tri (s, c):
    t.color (c)
    t.begin_fill ()
    for i in range (3):
        t.forward (s)
        t.left (120)
    t.end_fill ()

#ground
rec (250, 100, "#915a29")

#house
goto (25, 100)
rec (100, 100, "#8f2929")
goto (25, 200)
tri (100, "#f75e5e")

#tree
goto (175, 100)
rec (25, 100, "#876042")



t.mainloop ()