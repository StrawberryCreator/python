import random as r

score = []
scores1 = []
scores2 = []
scores3 = []
i = 0

for x in range (20):
    add = (r.randint (0, 100))
    while add in score:
        add = (r.randint (0, 100))
    score.append (add)

score.sort ()

while score[i] <= 30 and i != len(score) - 1:
    scores1.append (score[i])
    if i != len(score) - 1:
        i += 1
while score[i] > 30 and score[i] < 70 and i != len(score) - 1:
    scores2.append (score[i])
    if i != len(score) - 1:
        i += 1
while score[i] >= 70 and i != len(score) - 1:
    scores3.append (score[i])
    if i != len(score) - 1:
        i += 1

print ("-"* 50)
print ("scores =", score)
print ("0 - 30 |", scores1)
print ("31 - 69 |", scores2)
print ("70 - 100 |", scores3)
print ("-"* 50)