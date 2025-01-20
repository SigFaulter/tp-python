def process_input(user_input):
    try:
        user_input = int(user_input)
    except ValueError:
        print("Conversion en int est impossible")
        return None

    try:
        return user_input / 10
    except ZeroDivisionError:
        print("Division sur zero est impossible")
        return None

print(process_input("asdf"))
print(process_input("10"))
