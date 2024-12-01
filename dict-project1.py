marks = {
    "Uttaran": 100,
    "Tamoghna": 27,
    "Dhiraj": 13,
    "Udvah": 99,
    "Arjya": 69,
    "Rohan": 87,
    "Harsh": 89
}

a = input("Enter your name: ")
if a in marks:
    print(f"The marks of {a} is: {marks[a]}")
else:
    print(f"Sorry, {a}'s marks are not available.")