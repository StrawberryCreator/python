books = {"Romance" : 6.99, "Fantasy" : 8.99, "Physics" : 11.99}

print (books)
books["Physics"] = 12.99
books["Horror"] = 10.99
books["Action"] = 7.99
print (books)

book = input ("What book do you want to know the price of? ")
if book in books:
    print (books[book])
else:
    print ("Sorry i don't have that book")

print (books)