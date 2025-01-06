#create 2D list
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10,11,12]]

print (x)

#number of rows/columns
print ("Number of rows: ", len(x))
print ("Number of columns: ", len(x[1]))

#access elements
print (x[1][2])
print (x[3][2])

#looping trough values
for i in range (0, len(x)):
    for j in range (0, len(x[1])):
        print (x[i][j], end = " ")
    print ("\n")

#create 2D list with users inputs
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
y = []
for i in range (rows):
    temp = []
    for j in range (columns):
        z = int(input("Enter number: "))
        temp.append (z)
    y.append (temp)

print (y)

#add 2 2D lists
a = [[10, 11, 12], [13, 14, 15]]
b = [[1, 2, 3], [4, 5, 6]]

add = [[0, 0, 0], [0, 0, 0]]
sub = [[0, 0, 0], [0, 0, 0]]

for i in range (0, len(a)):
    for j in range (0, len(a[1])):
        add [i][j] = a[i][j] + b[i][j]
        sub [i][j] = a[i][j] - b[i][j]

print ("Add = ", add)
print ("Sub = ", sub)