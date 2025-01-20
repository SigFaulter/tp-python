def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("conversion est impossible")

print(convert_to_int("10"))
print(convert_to_int("test")) # doit declancher une erreur

