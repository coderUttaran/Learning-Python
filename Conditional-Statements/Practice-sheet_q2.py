mark1 = int(input("Enter the marks of first subject: "))
mark2 = int(input("Enter the marks of second subject: "))
mark3 = int(input("Enter the marks of third subject: "))
total_percentage = ((mark1 + mark2 + mark3) / 300)*100

if(total_percentage >=40):
    if(mark1 > 100 or mark2 > 100 or mark3 > 100):
        print("Invalid marks")
    elif(mark1 < 33 or mark2 < 33 or mark3 < 33):
        print(f"You are failed because of scoring below 33 in the subjects with: {total_percentage}% ")
    elif(mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
        print("You are passed with: ", total_percentage, "%")
else:
    print("You are failed with: ", total_percentage, "%")