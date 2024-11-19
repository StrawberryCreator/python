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

def cir (s, c):
    t.color (c)
    t.begin_fill ()
    t.circle (s)
    t.end_fill ()

#ground
rec (250, 100, "#915a29")

#house
goto (25, 100)
rec (100, 100, "#8f2929")
goto (25, 200)
tri (100, "#f75e5e")
#door
goto (40, 100)
rec (30, 55, "red")
#window
goto (90, 125)
rec (30, 30, "light blue")

#tree
goto (175, 100)
rec (25, 100, "#876042")
goto (187.5, 200)
cir (50, "green")

#grass
goto (0, 100)
for i in range (0, 250, 25):
    goto (i, 100)
    tri (25, "green")

t.hideturtle ()
t.mainloop ()