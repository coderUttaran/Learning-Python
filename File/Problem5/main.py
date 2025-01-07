words = ["donkey", "bad", "ganda"]

with open("file.txt") as f:
    content = f.read().lower()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)