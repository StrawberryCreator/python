import pgzrun as z
import random as rm

WIDTH = 500
HEIGTH = 500

def draw ():
    screen.fill ("light blue")
    r = Rect ((175, 50), (150, 400))
    screen.draw.filled_rect (r, "black")
    screen.draw.filled_circle ((250, 125), 50, "red")
    screen.draw.filled_circle ((250, 250), 50, "orange")
    screen.draw.filled_circle ((250, 375), 50, "green")

z.go ()