import turtle as t

t.bgcolor ("black")
t.color ("white")
t.speed (0)
sc = t.Screen ()
turtle = 1

def W ():
    t.setheading (90)
    t.forward (10)

def A ():
    t.setheading (180)
    t.forward (10)

def S ():
    t.setheading (270)
    t.forward (10)

def D ():
    t.setheading (0)
    t.forward (10)

def Pen ():
    global turtle
    if turtle == 1:
        t.hideturtle ()
        turtle = 0
    else:
        t.showturtle  ()
        turtle = 1

def gt (x, y):
    t.goto (x, y)
    t.write (name)

if str(input("do you want to write your name or draw?(write or draw) ")) == "draw":
    t.onkey (W, "w")
    t.onkey (A, "a")
    t.onkey (S, "s")
    t.onkey (D, "d")
    t.onkey (W, "Up")
    t.onkey (A, "Left")
    t.onkey (S, "Down")
    t.onkey (D, "Right")
    t.onkey (Pen, "space")
    t.listen ()
else:
    name = str(input("what is your name? "))
    t.penup ()
    sc.onclick (gt)
    t.onkey (Pen, "space")
    t.listen ()



t.mainloop ()