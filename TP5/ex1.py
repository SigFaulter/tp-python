i = 1
with open("exemple.txt", "r") as f:
    for line in f.readlines():
        print(f"{i} {line}", end='')
        i += 1

    f.close()
