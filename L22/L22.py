import pgzrun as pg
import random as r

WIDTH = 500
HEIGHT = 500
TITLE = "Shooting the alien"
msg = ""

alien = Actor ("alien.png")
alien.pos = r.randint (50, 450), r.randint (50, 450)

def draw ():
    screen.fill ("light blue")
    alien.draw ()
    screen.draw.text (msg, center = (250, 100))

def on_mouse_down (pos):
    global msg
    if alien.collidepoint (pos):
        msg = ("Great shot!")
        sounds.eep.play ()
        alien.pos = r.randint (50, 450), r.randint (50, 450)
    else:
        msg = "oops, missed."
        sounds.laugh.play ()

pg.go ()