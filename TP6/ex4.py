class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age est negatif")
    else:
        return age

try:
    set_age(-1)
except NegativeAgeError as e:
    print(f"Erreur: {e}")
