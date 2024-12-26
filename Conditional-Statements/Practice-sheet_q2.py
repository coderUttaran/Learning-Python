mark1 = int(input("Enter the marks of first subject: "))
mark2 = int(input("Enter the marks of second subject: "))
mark3 = int(input("Enter the marks of third subject: "))

if mark1 > 100 or mark1 < 0 or mark2 > 100 or mark2 < 0 or mark3 > 100 or mark3 < 0:
    print("Invalid marks entered, please enter marks between 0 and 100")
else:
    total_marks = mark1 + mark2 + mark3
    total_percentage = (total_marks / 300) * 100

    if(mark1 < 33 or mark2 < 33 or mark3 < 33):
        print("You have failed in the exam because you have scored less than 33% in one of the subjects")
    elif(total_percentage < 40):
        print("You have failed in the exam because you have scored less than 40% in total")
    else:
        print(f"Congratulations! You have passed the exam with {total_percentage}%")