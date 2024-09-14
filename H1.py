print("-"*50)
table = int(input("What table do you want to see? "))
print("-"*50)
num = 1
for i in range (table ,table * 10 + 1, table):
    print(num, "*", table, "=", i)
    num = num + 1
print("-"*50)