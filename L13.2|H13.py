import turtle as t

t.bgcolor ("black")

t1 = t.Turtle ()
t1.penup ()
t1.speed (0)
t1.shape ("square")
t1.color ("red", "black")
t1.goto  (-200, 200)
t1.pendown ()

t2 = t.Turtle ()
t2.penup ()
t2.speed (0)
t2.shape ("triangle")
t2.color ("yellow", "black")
t2.goto (200, 200)
t2.pendown ()

t3 = t.Turtle ()
t3.penup ()
t3.speed (0)
t3.shape ("circle")
t3.color ("green", "black")
t3.goto (-200, -200)
t3.pendown ()

t4 = t.Turtle ()
t4.penup ()
t4.speed (0)
t4.shape ("classic")
t4.color ("blue", "black")
t4.goto (200, -200)
t4.pendown ()

turtles = [t1, t2, t3, t4]

for x in range (37):
    t1.begin_fill ()
    for t1t in range (4):
        t1.forward (80)
        t1.right (90)
    t1.end_fill ()
    t1.right (10)
    t2.begin_fill ()
    for t2t in range (3):
        t2.forward (100)
        t2.right (120)
    t2.end_fill ()
    t2.right (10)
    t3.begin_fill ()
    for t3t in range (36):
        t3.forward (8)
        t3.right (10)
    t3.end_fill ()
    t3.right (10)
    t4.begin_fill ()
    for t4t in range (5):
        t4.forward (55)
        t4.right (72)
    t4.end_fill ()
    t4.right (10)



t.mainloop ()