age = int(input("Enter Your Age: "))
if(age>=0 and age<=3):
    print("You are infant")
elif(age>=3 and age<=12):
    print("You are child")
elif(age>=13 and age<=19):
    print("You are teenager")
elif(age>=20 and age<=30):
    print("You are young")
elif(age>=31 and age<=50):
    print("You are middle-aged")
elif(age>=51 and age<=65):
    print("You are old-middled-aged")
elif(age>=66):
    print("You are old")
else:
    print("Invalid Input")