marks = []
for x in range (1, 11, 1):
    Q = "What is student "
    Q += str(x)
    Q += " marks? "
    marks += input(Q)

total = 0
for x in (marks):
    total += int(x)
average = total / 10

print ("min =", min(marks))
print ("max =", max(marks))
print ("average =", average)
print ("total =", total)