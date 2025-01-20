import pgzrun as pg
import random as r

WIDTH = 500
HEIGHT = 500

score = 0

bee = Actor ("bee.png")
bee.pos = (250, 250)

flower = Actor ("flower.png")
flower.pos = (400, 100)

def draw ():
    global score
    screen.blit ("bg.png", (0, 0))
    bee.draw ()
    flower.draw ()
    screen.draw.text ("score: " + str(score), color = "black", topleft = (10, 10))

def update ():
    global score
    if keyboard.up:
        bee.y -= 2
    if keyboard.left:
        bee.x -= 2
    if keyboard.down:
        bee.y += 2
    if keyboard.right:
        bee.x += 2
    if bee.colliderect (flower):
        flower.pos = (r.randint (50, 450), r.randint (50, 450))
        score += 1

pg.go ()