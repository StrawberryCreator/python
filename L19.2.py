"""
Create a game dictionary
a)Get the user input name of a game and print its description.
b)Create a new entry for chess in the dictionary.
c)Change the description of cricket in the above dictionary
"""

games = {
    "soccer" : "Pass the ball to your teamates and try to shoot in the goal en avoid the goal keeper.",
    "volleyball" : "Keep the ball in the air and try to throw the ball onto the enemy's floor.",
    "cricket" : "One side taking a turn to bat a ball and score runs, while the other team will bowl and field the ball to restrict the opposition from scoring."
    }

game = input ("What game do you want to know more about? ")

if game in games:
    print (games[game])
else:
    print ("I'm sorry i dont know that game.")

games["chess"] = "Move your pieces and try to trap the king without killing him."

print (games)

games["cricket"] = "Cricket is played by two teams of 11, with one side taking a turn to bat a ball and score runs, while the other team will bowl and field the ball to restrict the opposition from scoring. The main objective in cricket is to score as many runs as possible against the opponent"
print (games)