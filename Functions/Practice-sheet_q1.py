def greatest(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif(c > a and c > b):
        return c
    else:
        return "All are equal"
    
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

print(greatest(a, b, c))