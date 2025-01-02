def inch_to_cms(inch):
    return inch * 2.54

n = float(input("Enter the value in inches: "))
print(f"{n} inches is equal to {inch_to_cms(n)} cms")