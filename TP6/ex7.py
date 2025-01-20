import logging

def log_error(message):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(message)

def read_file(filename):
    file = None
    try:
        file = open(filename, "r")
        return file.read()
    except FileNotFoundError:
        print(f"le fichier {filename} n'existe pas")
        log_error(f"le fichier {filename} n'existe pas")
    finally:
        if file:
            file.close()

print(read_file("ex3_not_found"))
print(read_file("ex3_file"))

