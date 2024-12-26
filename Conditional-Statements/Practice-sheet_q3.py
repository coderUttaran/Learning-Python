comment1 = "Make a lot of money"
comment2 = "buy now"
comment3 = "subscribe this"
comment4 = "click this"
comment = input("Enter your comment: ")
if(comment1 in comment or comment2 in comment or comment3 in comment or comment4 in comment):
    print("This is a spam comment")
else:
    print("This is not a spam comment")