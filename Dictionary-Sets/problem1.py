d = {
    "Uttaran": 100,
    "Udvah": 99,
    "Harsh": 99,
    "Abhphsita": 100,
}

new_student = input("Enter the name of the student: ")
new_marks = float(input("Enter the marks of the student: "))
d[new_student] = new_marks
print(d)

mark_update = input("Enter the name of the student whose marks you want to update: ")
if(mark_update not in d):
    print("Student not found")
else:
    new_marks = float(input("Enter the new marks of the student: "))
    d[mark_update] = new_marks
    print(d)

mark_delete = input("Enter the name of the student whose marks you want to delete: ")
if(mark_delete not in d):
    print("Student not found")
else:
    del d[mark_delete]
    print(d)