vowels = {"a" : 0, "e" : 0, "o" : 0, "u" : 0, "i" : 0}

word = (input ("Input your word ")).lower ()

for x in word:
    if x in vowels:
        vowels[x] += 1

print (vowels)