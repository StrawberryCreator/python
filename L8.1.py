import turtle as t

t.bgcolor ("black")
t.color ("white")

def forward ():
    t.forward (10)

def R ():
    t.setheading (0)

def L ():
    t.setheading (180)

def U ():
    t.setheading (90)

def D ():
    t.setheading (270)

t.onkey (forward, "space")
t.onkey (R, "Right")
t.onkey (L, "Left")
t.onkey (U, "Up")
t.onkey (D, "Down")

t.listen ()

t.mainloop ()