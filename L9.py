import turtle as t
import random as r

t.bgcolor ("black")

def user_move ():
    user.forward (15)

#create player
user = t.Turtle ()
user.shape ("turtle")
user.color ("white")
user.penup ()
user.goto (-200, 200)

#create bots
colors = ["red", "yellow", "green", "blue"]
bots = []
yPos = 100
for x in colors:
    bot = t.Turtle ()
    bots.append (bot)
    bot.shape ("turtle")
    bot.color (x)
    bot.penup ()
    bot.goto (-200, yPos)
    yPos -= 100

while True:
    for activeBot in bots:
        activeBot.forward (r.randint (1, 20))
    t.onkey (user_move, "space")
    t.listen ()
    if activeBot.xcor () >= 200:
        break
    if user.xcor () >= 200:
        break

t.mainloop ()