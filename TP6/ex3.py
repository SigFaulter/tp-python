def read_file(filename):
    file = None
    try:
        file = open(filename, "r")
        return file.read()
    except FileNotFoundError:
        print(f"le fichier {filename} n'existe pas")
    finally:
        if file:
            file.close()

print(read_file("ex3_not_found"))
print(read_file("ex3_file"))

