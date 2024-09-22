#even numbers 0 to 50.
x = 0
while x <= 50:
    print (x)
    x += 2
print ("-"*50)
#1 to 30 if number in the table of 3 say BINGO
x = 1
while x <= 30:
    if x % 3 == 0:
        print ("bingo")
    else:
        print (x)
    x += 1
print ("-"*50)
#multible of any table
table = int(input("What table do you want to see? "))
print("- "*25)
num = 1
x = table
while x <= table * 10:
    print (num, "*", table, "=", x)
    x += table
    num += 1
print("-"*50)