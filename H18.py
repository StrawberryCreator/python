import turtle as t
import random as r

t.bgcolor ("black")

score = 0

t.speed (0)
t.hideturtle ()

def border ():
    t.color ("red")
    t.penup ()
    t.goto (-250, 250)
    t.pendown ()
    t.goto (250, 250)
    t.goto (250, -250)
    t.goto (-250, -250)
    t.goto (-250, 250)

border ()

player = t.Turtle ()
player.color ("white")
player.shape ("square")
player.speed (0)
player.penup ()
player.goto (0, -100)

coin = t.Turtle ()
coin.color ("yellow")
coin.shape ("circle")
coin.speed (0)
coin.penup ()
coin.goto (0, 100)

def w ():
    y = player.ycor ()
    if y <= 230:
        player.setheading (90)
        player.forward (20)
        check ()

def a ():
    x = player.xcor ()
    if x >= -230:
        player.setheading (180)
        player.forward (20)
        check ()

def s ():
    y = player.ycor ()
    if y >= -230:
        player.setheading (270)
        player.forward (20)
        check ()

def d ():
    x = player.xcor ()
    if x <= 230:
        player.setheading (0)
        player.forward (20)
        check ()

t.listen ()
t.onkey (w, "w")
t.onkey (a, "a")
t.onkey (s, "s")
t.onkey (d, "d")

def printScore ():
    t.clear ()
    border ()
    t.penup ()
    t.color ("white")
    t.goto (0, 250)
    t.write (score, font=("arial", 25, "normal"))

printScore ()

def moveCoin ():
    coin.goto (round(r.randint(-250, 250)/20)*20, round(r.randint(-250, 250)/20)*20)

def check ():
    global score
    if player.distance (coin) < 19:
            score += 1
            printScore ()
            moveCoin ()

t.mainloop ()