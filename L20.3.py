numbers = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}

num = input ("Input your number ")

for x in num:
    if x in numbers:
        numbers[x] += 1

pangram = True
for x in numbers.values ():
    if x == 0:
        pangram = False

if pangram:
    print ("It is a pangram")
else:
    print ("It is not a pangram")
