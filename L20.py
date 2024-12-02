"""
Write a program that uses a dictionary that contains ten usernames and passwords. 
The program should ask the user to enter their username and password. 
If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system. 
If the username is in the dictionary, but the user does not enter the right password, the program should say that the password is invalid. 
If the password is correct, then the program should tell the user that they are now logged in to the system.
"""

accounts = {"user1" : "123", "user2" : "abc", "user3" : "456", "user4" : "def", "user5" : "789"}

username = input ("Username: ")
password = input ("Password: ")

if username not in accounts:
    print ("Username not detected in system.")
else:
    if accounts[username] == password:
        print ("You succesfully logged in.")
    else:
        print ("Password is incorrect.")