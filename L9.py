import turtle as t
import random as r

t.bgcolor ("black")

def user_move ():
    user.forward (15)

def move_bot () :
    activeBot.forward (r.randint (1, 25))

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

t.onkey (user_move, "space")
t.listen ()

won = False
while not won: 
    for activeBot in bots:
        move_bot ()
        if activeBot.xcor () >= 200:
            won = True
            winner = activeBot.color () [0]
            break
        if user.xcor () >= 200:
            won = True
            winner = "white"
            break

if winner:
    t.color ("white")
    t.write ("The " + winner + " turtle wins!", font= ("Ariel", 20, "bold"))

t.mainloop ()
