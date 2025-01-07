from os import remove

with open("file.txt") as f:
    content = f.read()

with open("renamed.txt", "w") as f:
    f.write(content)
    
remove("file.txt")