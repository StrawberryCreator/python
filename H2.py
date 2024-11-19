import turtle as t

t.speed (0)
t.width (10)
t.penup ()
t.goto (0, -50)
t.pendown ()

bgColor = input("What color do you want the background to be? ")
t.bgcolor (bgColor)

outColor = input("What color do you want the outline of the circle to be? ")
color = input("What color do you want the circle to be? ")

t.color (outColor, color)

t.begin_fill ()
t.circle (100)
t.end_fill ()

t.mainloop ()