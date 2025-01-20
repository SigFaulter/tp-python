def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division sur zero est impossible")
        return None
    else:
        print("Division effectuee avec succes")
    finally:
        print("Fonction terminee")

print(safe_division(1, 0)) # diviser par 0
print(safe_division(1, 4)) # diviser un autre nombre

