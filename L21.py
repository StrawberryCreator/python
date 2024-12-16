import pgzrun
import random as rm

HEIGTH = 500
WIDTH = 500

def draw ():
    screen.fill ("black")
    h = 100
    w = 200
    for x in range (10):
        r = rm.randint (0, 255)
        g = rm.randint (0, 255)
        b = rm.randint (0, 255)
        c = (r, g, b)
        r = Rect ((100, 100), (w, h))
        r.center = (WIDTH/2, HEIGTH/2)
        screen.draw.rect (r, c)
        h += 5
        w -= 10
    screen.draw.line ((50, 50), (50, 200), "white")
    screen.draw.circle ((50, 150), 25, "blue")
    screen.draw.filled_circle ((50, 175), 10, "light blue")


pgzrun.go ()