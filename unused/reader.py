with open('file.txt', "r") as f:
    value = int(f.read())
with open("file.txt", "w") as f:
    f.write(str(value + 1))
with open('file.txt', "r") as f:
    print(f.read())
