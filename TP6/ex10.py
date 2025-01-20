while True:
    file_to_read = input("Saisir un fichier pour le lire: ")

    try:
        file = open(file_to_read, "r")
        print(file.read())
    except FileNotFoundError:
        print(f"le fichier {file_to_read} n'existe pas")
        continue

    number = input("Donner un entier: ")

    try:
        number = int(number)
    except ValueError:
        print("Conversion en int est impossible")
        continue

    break
