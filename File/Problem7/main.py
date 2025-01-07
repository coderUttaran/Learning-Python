with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("Python is not present in the file")