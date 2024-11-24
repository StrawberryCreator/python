import turtle as t
import random as r

t.bgcolor ("black")

score = 0

t.speed (0)
t.hideturtle ()

def enemyBorder ():
    t.color ("yellow")
    t.penup ()
    t.goto (-325, 325)
    t.pendown ()
    t.goto (325, 325)
    t.goto (325, -325)
    t.goto (-325, -325)
    t.goto (-325, 325)

def playerBorder ():
    t.color ("red")
    t.penup ()
    t.goto (-250, 250)
    t.pendown ()
    t.goto (250, 250)
    t.goto (250, -250)
    t.goto (-250, -250)
    t.goto (-250, 250)

playerBorder ()
enemyBorder ()

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
    playerBorder ()
    enemyBorder ()
    t.penup ()
    t.color ("white")
    t.goto (0, 275)
    t.write (score, font=("arial", 25, "normal"))

printScore ()

def moveCoin ():
    coin.goto (round(r.randint(-250, 250)/20)*20, round(r.randint(-250, 250)/20)*20)

enemies = []
def spawnEnemy ():
    global enemies
    newEnemy = t.Turtle ()
    newEnemy.color ("red")
    newEnemy.shape ("classic")
    newEnemy.speed (0)
    newEnemy.penup ()
    x = r.randint (-315, 315)
    y = r.randint (-315, 315)
    spawnable = not(x > -260 and x < 260 and y > -260 and y < 260)
    while not(spawnable):
        x = r.randint (-315, 315)
        y = r.randint (-315, 315)
        spawnable = not(x > -260 and x < 260 and y > -260 and y < 260)
    newEnemy.goto (x, y)
    enemies += [newEnemy]

def hideAllTurtles ():
    player.hideturtle ()
    coin.hideturtle ()
    for x in (enemies):
        x.hideturtle ()
    deathMessage ()

def deathMessage ():
    global score
    t.clear ()
    t.goto (-225, 0)
    t.color ("red")
    t.write ("YOU DIED", font=("arial", 100, "normal"))
    t.goto (-75, -100)
    t.color ("white")
    deathMessage = "score: "
    deathMessage += str(score)
    t.write (deathMessage, font=("arial", 50, "normal"))

def check ():
    global score
    moveEnemies ()
    if player.distance (coin) < 19:
            score += 1
            printScore ()
            moveCoin ()
            spawnEnemy ()
    for x in (enemies):
        if player.distance (x) < 20:
                hideAllTurtles ()

def moveEnemies ():
    global enemies
    for x in (enemies):
        x.setheading(x.towards (player.xcor (), player.ycor ()))
        x.setheading (round(x.heading()/90)*90)
        x.forward (10)
        x.goto (round(x.xcor()/10)*10, round(x.ycor()/10)*10)

t.mainloop ()