a = [[1, 2], [3, 4]]
b = [[10, 11], [12, 13]]

c = [[0, 0], [0, 0]]

for i in range (0, 2):
    for j in range (0, 2):
        for k in range (0, 2):
            c[i][j] = c[i][j] + (a[i][k] * b[k][j])

print (c)