import turtle as t

t.bgcolor ("black")
t.color ("white")
t.speed (0)

def od (x, y):
    t.ondrag (None)
    t.setheading (t.towards (x, y))
    t.goto (x, y)
    t.ondrag (od)

t.ondrag (od)

t.mainloop ()