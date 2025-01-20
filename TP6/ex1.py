def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division sur zero est impossible")

print(safe_division(1, 0)) # diviser par 0
print(safe_division(1, 4)) # diviser un autre nombre

