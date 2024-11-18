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


def check ():
     global tails
     if snake.distance (apple) < 20:
          appleRand ()
          global score
          score += 1
          t.clear ()
          t.write (score, font= ("Arial", 40, "normal"))
          new_tail = t.Turtle ()
          new_tail.shape ("square")
          new_tail.color ("gray")
          new_tail.penup ()
          tails.append (new_tail)
          print (len(tails))
          for i in range (len(tails)-1, 0,-1) :
               x = tails [i-1].xcor ()
               y = tails [i-1].ycor ()
               tails[i].goto (x,y)
          if (len(tails) > 0) :
              x = snake.xcor ()
              y = snake.ycor ()
              tails [0].goto (x,y)
        
        
    
def appleRand ():
    apple.goto (round(r.randint (-200, 200)/20)*20, round(r.randint (-200, 200)/20)*20)

snake.directions = "stop"

def movement_snake () :
    if snake.directions == "up" :
        y = snake.ycor ()
        snake.sety (y + 5)
        check ()
    if snake.directions == "down" :
        y = snake.ycor ()
        snake.sety (y - 5)
        check ()
    if snake.directions == "left" :
        x = snake.xcor ()
        snake.setx (x - 5)
        check ()
    if snake.directions == "right" :
        x = snake.xcor ()
        snake.setx (x + 5)
        check ()

def W ():
    snake.directions = "up"
    

def A ():
    snake.directions = "left"

def S ():
    snake.directions = "down"

def D ():
    snake.directions = "right"

t.listen ()
t.onkey (W, "w")
t.onkey (A, "a")
t.onkey (S, "s")
t.onkey (D, "d")

while True :
    t.update ()
    movement_snake ()

t.mainloop ()