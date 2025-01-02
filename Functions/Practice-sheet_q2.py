def f_to_c(f):
    return 5*(f-32)/9

f = float(input("Enter the temperature in Fahrenheit: "))

print(f"The temperature in Celsius: {f_to_c(f)}")