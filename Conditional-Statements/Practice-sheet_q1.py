a1 = float(input("Enter the No. 1: "))
a2 = float(input("Enter the No. 2: "))
a3 = float(input("Enter the No. 3: "))
a4 = float(input("Enter the No. 4: "))

if (a1 > a2 and a1 > a3 and a1 > a4):
    print(f"{a1} is the greatest number.")
elif (a2 > a1 and a2 > a3 and a2 > a4):
    print(f"{a2} is the greatest number.")
elif (a3 > a1 and a3 > a2 and a3 > a4):
    print(f"{a3} is the greatest number.")
else:
    print(f"{a4} is the greatest number.")