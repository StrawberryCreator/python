import turtle as t
import random as r
import time as m

t.bgcolor ("light blue")

height = 0
wallHeight = 0
maxX = 500
wallX = maxX
score = 0
pastHeight = 10
pastWallHeight = 9
running = True

head = t.Turtle ()
head.color ("orange")
head.shape ("square")
head.speed (0)
head.penup ()
head.goto (0, -90)

tails = []
tailY = -90
for x in range (10):
    newTails = t.Turtle ()
    newTails.color ("yellow")
    newTails.shape ("square")
    newTails.speed (0)
    newTails.penup ()
    newTails.goto (0, tailY)
    tailY += 20
    tails += [newTails]

def tailsUpdate ():
    global pastHeight
    if height != pastHeight:
        for x in range (height):
            tails[x].showturtle ()
        for x in range (height, pastHeight, 1):
            tails[x].hideturtle ()
        head.goto (0, height * 20 - 90)
    pastHeight = height

tailsUpdate ()

walls = []
wallY = -90
for x in range (9):
    newWall = t.Turtle ()
    newWall.color ("dark green")
    newWall.shape ("square")
    newWall.speed (0)
    newWall.penup ()
    newWall.goto (wallX-10, wallY)
    wallY += 20
    walls += [newWall]

def wallsUpdate ():
    global pastWallHeight
    for x in range (wallHeight, pastWallHeight, 1):
        walls[x].hideturtle ()
    for x in range (wallHeight):
        walls[x].setx (wallX)
    for x in range (wallHeight):
        walls[x].showturtle ()
    pastWallHeight = wallHeight

wallsUpdate ()

groundT = t.Turtle ()
groundT.speed (0)
groundT.color ("green")
groundT.hideturtle ()

def ground ():
    groundT.penup ()
    groundT.goto (-30, -100)
    groundT.begin_fill ()
    groundT.goto (maxX, -100)
    groundT.goto (maxX, -200)
    groundT.goto (-30, -200)
    groundT.goto (-30, -100)
    groundT.end_fill ()

ground ()

def playerUp ():
    global height
    if height < 10:
        height += 1
    tailsUpdate ()

t.onkey (playerUp, "space")
t.listen ()

def clearAll ():
    for x in range (10):
        tails[x].hideturtle ()
    head.hideturtle ()
    groundT.clear ()
    scoreT.clear ()
    while True:
        for x in range (9):
            walls[x].hideturtle ()

deathMessageT = t.Turtle ()
deathMessageT.color ("red")
deathMessageT.speed (0)
deathMessageT.hideturtle ()
deathMessageT.penup ()
deathMessageT.goto (-250, 50)

def deathMessage ():
    t.bgcolor ("black")
    deathMessageT.write ("YOU DIED", font=("arial", 100, "normal"))
    deathMessageT.goto (-100, -50)
    deathMessageT.color ("white")
    deathMessage = "score: "
    deathMessage += str(score)
    deathMessageT.write (deathMessage, font=("arial", 50, "normal"))

def lose ():
    global running
    running = False
    deathMessage ()
    clearAll ()

scoreT = t.Turtle ()
scoreT.color ("white")
scoreT.speed (0)
scoreT.hideturtle ()
scoreT.penup ()
scoreT.goto (-200, 200)

scoreMessage = "score: "
scoreMessage += str(score)
scoreT.write (scoreMessage, font=("arial", 50, "normal"))

def writeScore ():
    scoreMessage = "score: "
    scoreMessage += str(score)
    scoreMessage += " ("
    scoreMessage += precision
    if precision == "perfect":
        scoreMessage += " +2)"
        scoreT.color ("blue")
    else:
        scoreMessage += " +1)"
        scoreT.color ("green")
    scoreT.clear ()
    scoreT.write (scoreMessage, font=("arial", 50, "normal"))

winMessageT = t.Turtle ()
winMessageT.color ("green")
winMessageT.speed (0)
winMessageT.hideturtle ()
winMessageT.penup ()
winMessageT.goto (-250, 50)

def winMessage ():
    t.bgcolor ("black")
    winMessageT.write ("YOU WON", font=("arial", 100, "normal"))
    winMessageT.goto (-100, -50)
    winMessageT.color ("white")
    winMessage = "score: "
    winMessage += str(score)
    winMessageT.write (winMessage, font=("arial", 50, "normal"))

def win ():
    global running
    running = False
    winMessage ()
    clearAll ()

wallHeight = r.randint (1, 9)
while running:
    if wallX >= -10 and wallX <= 10:
        if height > wallHeight:
            score += 1
            precision = "good"
            height = height - wallHeight
            writeScore ()
        elif height == wallHeight:
            score += 2
            precision = "perfect"
            height = height - wallHeight
            writeScore ()
        else:
            lose ()
        tailsUpdate ()
        wallX -= 20
    elif wallX >= -10:
        wallX -= 20
    else:
        if maxX >= 70:
            maxX -= 20
            groundT.clear ()
            ground ()
            wallHeight = r.randint (1, 9)
            wallX = maxX
        else:
            win ()
    wallsUpdate ()
    for x in range (9):
        m.sleep (0.001)

t.mainloop ()