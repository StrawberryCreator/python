import pgzrun as pg
import random as r

WIDTH = 600
HEIGHT = 600

game = True
lose = False
win = False
render = True
editPlayerHeight = False
playerHeight = 1
wallHeight = r.randint (3, 6)
wallX = 550
speed = 1
score = 0
scoreType = ""

head = Actor ("head.png")
head.x = (150)

body = Actor ("body.png")
body.x = (150)

wall = Actor ("wall.png")
wall.x = (500)

eggs = Actor ("eggs.png")
eggs.pos = (500, 475)

def draw ():
    global render
    if render and game:
        screen.clear ()
        screen.blit ("bg.png", (0, 0))
        renderPlayer (playerHeight)
        renderWall (wallHeight)
        screen.draw.text (str(score), midtop = (300, 20))
        if scoreType == "Hit!":
            screen.draw.text ("Hit! (-5)", midtop = (300, 40))
        if scoreType == "Perfect!":
            screen.draw.text ("Perfect! (+10)", midtop = (300, 40))
        if scoreType == "Good":
            screen.draw.text ("Good (+5)", midtop = (300, 40))
        render = False
    if not(game):
        screen.clear ()
        if lose:
            screen.draw.text ("You lose!", fontsize = 100, color = "red", midtop = (300, 250))
            screen.draw.text (str(score), fontsize = 50, midtop = (300, 350))
        if win:
            screen.blit ("bg.png", (0, 0))
            screen.draw.text ("You win!", fontsize = 100, color = "green", midtop = (300, 250))
            screen.draw.text (str(score), fontsize = 50, midtop = (300, 350))
            eggs.draw ()
            for x in range (400):
                head.pos = (450, 475)
                head.draw ()

def renderPlayer (height):
    for x in range (height-1):
        body.y = (475 - x*50)
        body.draw ()
    head.y = (525 - height*50)
    head.draw ()

def renderWall (height):
    for x in range (height):
        wall.pos = (wallX, 475 - x*50)
        wall.draw ()

def moveWall ():
    global wallX
    global wallHeight
    global speed
    global render
    global editPlayerHeight
    global playerHeight
    if editPlayerHeight:
        playerHeight -= wallHeight
        editPlayerHeight = False
    if wallX <= 50:
        if speed <= 0.125:
            youWin ()
        else:
            speed -= 0.1
            wallX = 550
            wallHeight = r.randint (1, 9)
    else:
        wallX -= 50
    if wallX == 150:
        checkHeight ()
    render = True
    if game:
        clock.schedule (moveWall, speed)

def hit ():
    global playerHeight
    global render
    playerHeight = 1
    render = True

def checkHeight ():
    global score
    global scoreType
    global render
    global editPlayerHeight
    global playerHeight
    if playerHeight == wallHeight:
        if score > 0:
            score -= 5
            clock.schedule (hit, speed)
        else:
            clock.schedule (youLose, 1)
        scoreType = "Hit!"
        playerHeight = wallHeight+1
    elif playerHeight == wallHeight+1:
        score += 10
        scoreType = "Perfect!"
        editPlayerHeight = True
    elif playerHeight > wallHeight+1:
        score += 5
        scoreType = "Good"
        editPlayerHeight = True
    elif playerHeight < wallHeight:
        youLose ()
    render = True

def youWin ():
    global game
    global win
    game = False
    win = True
    print ("you win")

def youLose ():
    global game
    global lose
    game = False
    lose = True
    print ("you lose!")

def update ():
    pass

def on_mouse_down ():
    global playerHeight
    global render
    if playerHeight <= 9:
        playerHeight += 1
        render = True

clock.schedule (moveWall, speed)

pg.go ()