#dictionaries

#empty dict
dict = {}

#create dict
cc = {"Netherlands" : "Amsterdam", "UK" : "Londen", "USA" : "Washington DC", "India" : "New Delhi"}

#get value from key
print (cc["Netherlands"])
#avoid errors
print (cc.get("dutch", "Unknown"))

#add element
cc["Greece"] = "Athena"
print (cc)

#displaye all the keys as list
print (cc.keys ())
#values
print (cc.values ())

#get length
print (len (cc))

#check if keys exits
print ("Sri Lanka" in cc)
print ("Netherlands" in cc)

#delet element
del cc ["India"]
print (cc)

#modify value
cc["Greece"] = "ATHENA"
print (cc)

#iteration
list = []
for x in cc:
    list.append (x)
print (list)
list.sort ()
print (list)