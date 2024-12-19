keep_writing = True
list_strings = []

while keep_writing:
    list_strings.append(str(input("Donner une phrase a ecrire: ")) + "\n")
    confirmation = input("Souhaitez-vous ecrire une autre phrase? (oui/non): ")
    if confirmation.lower() == "non":
        break
    elif confirmation.lower() != "oui":
        print("Veuillez repondre par oui ou par non")


with open("phrases.txt", "a") as f:
    f.writelines(list_strings)
    f.close()

