money = float(input("How much money do you have? "))

if money >= 24:
    print ("You can buy the socks and the pants")
elif money >= 20:
    print ("You can buy the pants or the socks")
elif money >= 4:
    print ("You can buy the socks")
else:
    print ("You can't buy anything :(")