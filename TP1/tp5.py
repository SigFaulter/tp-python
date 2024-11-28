def factorielle(n):
    if n == 1:
        return n
    return factorielle(n - 1) * n

print(factorielle(4))

