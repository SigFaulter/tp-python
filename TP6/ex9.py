def get_positive_integer():
    while True:
        data = input("Donner un entier positif: ")
        try:
            data = int(data)
        except ValueError as e:
            print(f"Entree invalide: {e}")
            continue

        if data < 0:
            print("Entier n'est pas positif")
        else:
            break

get_positive_integer()

