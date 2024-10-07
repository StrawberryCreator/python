import random as r
chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "§", "±", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", '"', '/', "|", "`", "~", ",", "<", ".", ">", "/", "?"]
password = ""
while True:
    length = int(input("what do you want the length of your password? "))
    for x in range (length):
        password += chars [r.randint (0, len (chars)-1)]
    print (password)
    if input("Do you want to create another password (y/n)? ") == "n":
        break