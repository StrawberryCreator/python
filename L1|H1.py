import turtle as t

t.bgcolor ("light blue")

t.color ("white")
t.speed (0)
t.hideturtle ()

t.penup ()
t.goto (0, -250)
t.begin_fill ()
t.circle (130)
t.end_fill ()

t.goto (0, -50)
t.begin_fill ()
t.circle (90)
t.end_fill ()

t.goto (0, 100)
t.begin_fill ()
t.circle (60)
t.end_fill ()

t.color ("black")

t.goto (0, 70)
t.begin_fill ()
t.circle (10)
t.end_fill ()

t.goto (0, 40)
t.begin_fill ()
t.circle (10)
t.end_fill ()

t.goto (0, 10)
t.begin_fill ()
t.circle (10)
t.end_fill ()

t.goto (-25, 175)
t.begin_fill ()
t.circle (10)
t.end_fill ()

t.goto (25, 175)
t.begin_fill ()
t.circle (10)
t.end_fill ()

t.goto (-19, 133)
t.begin_fill ()
t.circle (2)
t.end_fill ()

t.goto (-14, 128)
t.begin_fill ()
t.circle (2)
t.end_fill ()

t.goto (-7, 125)
t.begin_fill ()
t.circle (2)
t.end_fill ()

t.goto (0, 125)
t.begin_fill ()
t.circle (2)
t.end_fill ()

t.goto (7, 125)
t.begin_fill ()
t.circle (2)
t.end_fill ()

t.goto (14, 128)
t.begin_fill ()
t.circle (2)
t.end_fill ()

t.goto (19, 133)
t.begin_fill ()
t.circle (2)
t.end_fill ()

t.color ("orange")

t.goto (-5, 165)
t.begin_fill ()
t.goto (25, 155)
t.goto (-5, 145)
t.goto (-5, 165)
t.end_fill ()

t.showturtle ()
t.color ("brown")
t.width (5)

t.goto (-75, 90)
t.pendown ()
t.goto (-125, -25)
t.penup ()

t.goto (75, 90)
t.pendown ()
t.goto (175, 175)
t.penup ()

t.mainloop ()