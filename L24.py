"""
Create a program that will al low the user to easily manage a list of names.
You should display a menu that will allow them to add a name to the list,
change a name in the list, delete a name from the list or view all the names in the list.
There should also be a menu option to allow the user to end the program.
If they select an option that is not relevant, then it should display a suitable message.
After they have made a selection to either add a name, change a name,
delete a name or view all the names,
they should see the menu again without having to restart the program.
The program should be made as easy to use as possible.
"""

names = []

print ("Welcome")

while True:
    action = input("What do you want to do ('?' for actions)? | ")

    if action == "?":
        print ("Actions:")
        print ("1. Add name")
        print ("2. Remove name")
        print ("3. Change name")
        print ("4. View all names")
        print ("5. End program")
    elif action == "1":
        value = input("What name do you want to add? | ")
        names.append (value)
    elif action == "2":
        value = input("What name or name number do you want to delete? | ")
        if value in names:
            names.pop (names.index (value))
        else:
            names.pop (value)
    elif action == "3":
        value1 = input("What name or name number do you want to change? | ")
        value2 = input("To what do you want to replace it? | ")
        if value1 in names:
            names [names.index (value1)] = value2
        else:
            names [int(value1)] = value2
    elif action == "4":
        nameDis = " | "
        for i in range (0, len(names), 1):
            nameDis += names[i]
            nameDis += " | "
        print (nameDis)
    elif action == "5":
        break
    else:
        print ("This command is unknown try '?' and pick the number of the command you want.")

print ("Bye!")