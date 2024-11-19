#say the table the user wants
print("-"*50)
table = int(input("What table do you want to see? "))
print("- "*25)
num = 1
for x in range (table ,table * 10 + 1, table):
    print(num, "*", table, "=", x)
    num += 1
print("-"*50)