import turtle as t

t.bgcolor ("black")
t.color ("white")

sc = t.Screen ()

def gt (x, y):
    t.goto (x, y)
    t.write (str(x)+ ", "+ str(y))

t.penup ()
sc.onclick (gt)

t.mainloop ()