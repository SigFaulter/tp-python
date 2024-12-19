import csv

with open("contacts.csv", "r") as f:
    reader = csv.reader(f)
    next(reader) # skip first line as it contains headers
    for line in reader:
        print(f"Nom: {line[0]}, Age: {line[1]}, Ville: {line[2]}")
