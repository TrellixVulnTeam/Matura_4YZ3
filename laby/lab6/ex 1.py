li = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def suma(n):
    if n == 0: return 0
    return suma(n - 1) + n


print(suma(3))
