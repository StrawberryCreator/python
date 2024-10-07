import random as r
choices = ["rock", "paper", "scissors"]
round = 0
computer_win = 0
user_win = 0
print("-"*50)
rounds = int(input("How many rounds do you want to play? "))
while True:
    round += 1
    print("-"*50)
    print ("round", round)
    print ("- "*25)
    print ("1. rock")
    print ("2. paper")
    print ("3. scissors")
    print ("- "*25)
    user_choice = int(input("user choice: "))
    computer_choice = r.randint (1, 3)
    print ("computer choice:", computer_choice)
    print ("- "*25)
    if user_choice == computer_choice:
        print ("tie")
    elif user_choice == 1 and computer_choice == 2:
        print ("computer wins")
        computer_win += 1
    elif user_choice == 2 and computer_choice == 3:
        print ("computer wins")
        computer_win += 1
    elif user_choice == 3 and computer_choice == 1:
        print ("computer wins")
        computer_win += 1
    elif computer_choice == 1 and user_choice == 2:
        print ("user wins")
        user_win += 1
    elif computer_choice == 2 and user_choice == 3:
        print ("user wins")
        user_win += 1
    elif computer_choice == 3 and user_choice == 1:
        print ("user wins")
        user_win += 1
    print ("- "*25)
    print ("computer wins:", computer_win)
    print ("user wins:", user_win)
    if round == rounds:
        break
print("-"*50)
if user_win > computer_win:
    print ("user wins with ", user_win, "-", computer_win)
elif computer_win > user_win:
    print ("computer wins with ", computer_win, "-", user_win)
else:
    print ("it's a tie it was ", user_win, "-", computer_win)
print("-"*50)