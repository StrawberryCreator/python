import turtle as t
import random as r
import time as m

t.bgcolor ("black")

score = 0
tails = []
pastX = []
pastY = []
t.color ("white")
t.penup ()
t.goto (0, 275)
t.hideturtle ()
t.write (score, font= ("Arial", 40, "normal"))

snake = t.Turtle ()
snake.speed (0)
snake.shape ("square")
snake.color ("white")
snake.penup ()
snake.goto (-100, 100)


apple = t.Turtle ()
apple.speed (0)
apple.shape ("circle")
apple.color ("red")
apple.penup ()
apple.goto (100, 100)


def W ():
    y = snake.ycor ()
    snake.sety (y + 20)
    check ()

def A ():
    x = snake.xcor ()
    snake.setx (x - 20)
    check ()

def S ():
    y = snake.ycor ()
    snake.sety (y - 20)
    check ()

def D ():
    x = snake.xcor ()
    snake.setx (x + 20)
    check ()

def check ():
    global tails
    global pastX
    pastX += [snake.xcor ()]
    pastX.remove [len(tails)-1]
    global pastY
    pastY += (snake.ycor ())
    if snake.distance (apple) < 20:
        appleRand ()
        global score
        score += 1
        t.clear ()
        t.write (score, font= ("Arial", 40, "normal"))
        tails += [t.Turtle ()]
        tails[len(tails)-1].shape ("square")
        tails[len(tails)-1].color ("gray")
        tails[len(tails)-1].penup ()
        tails[len(tails)-1].speed (0)
        
    
def appleRand ():
    apple.goto (round(r.randint (-200, 200)/20)*20, round(r.randint (-200, 200)/20)*20)

t.listen ()
t.onkey (W, "w")
t.onkey (A, "a")
t.onkey (S, "s")
t.onkey (D, "d")

t.mainloop ()