#create list and set values
color = ["red", "yellow", "green", "blue", "pink", "black"]
print (color)

#get length of list
print (len(color))

#get value from position (index)
print (color[3])

#replace value
color [4] = "purple"
print (color)

#check if value stored
if "pink" in color:
    print ("Yes, pink is in the list color")
else:
    print ("no, pink is not in the list color")

if "purple" in color:
    print ("Yes, purple is in the list color")
else:
    print ("no, purple is not in the list color")

#print values in list after sepreatly
for x in color:
    print (x)

#remove item
color.remove ("black")
print (color)

#count number of times the value is in the list
print (color.count("red"))

#get the position of item in list
print (color.index ("yellow"))

#reverse the list
color.reverse ()
print (color)

#sort list
color.sort ()
print (color)

#join lists together
color2 = ["white", "black"]
color.append (color2)
print (color2)
print (color)