with open("phrases.txt", "w") as f:
    for i in range(3):
        f.write(str(input("Donner une phrase a ecrire: ")) + "\n")

f.close()

