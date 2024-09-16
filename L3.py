import random as r
print ("welcome to sebbe's supermarket!")
totalPrice = 0
total = 0
while True :
    print ("1. drinks")
    print ("2. food")
    print ("3. clothes")
    print ("4. tools")
    print ("5. toys")
    choice = int(input("what do you want to buy? (1-5) "))
    if choice == 1:
        price = r.randint (1, 15)
        amount = int(input("how many do you want to purches? "))
        total = price * amount
        print ("the total is", total)
    if choice == 2:
        price = r.randint (2, 35)
        amount = int(input("how many do you want to purches? "))
        total = price * amount
        print ("the total is", total)
    if choice == 3:
        price = r.randint (6, 45)
        amount = int(input("how many do you want to purches? "))
        total = price * amount
        print ("the total is", total)
    if choice == 4:
        price = r.randint (10, 40)
        amount = int(input("how many do you want to purches? "))
        total = price * amount
        print ("the total is", total)
    if choice == 5:
        price = r.randint (5, 25)
        amount = int(input("how many do you want to purches? "))
        total = price * amount
        print ("the total is", total)
    totalPrice += total
    stop = input("was that everything? (y/n) ")
    if stop == "y":
        print ("your total is €", totalPrice)
        print ("bye, thanks for shopping in sebbe's supermarket!")
        break