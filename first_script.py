with open("my_file.txt", "w") as f:
    for i in range(1,5):
        f.write(str(i))

with open("my_file.txt", "w") as f:
    for i in range(6,10):
        f.write(str(i))

with open("my_file.txt", "r") as f:
    print(f.read())
