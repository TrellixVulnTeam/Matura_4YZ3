def pierwsza(n):
    t = True
    if n == 1:
        return False
    for x in range(2, int(n ** (1 / 2) + 1)):
        if n % x != 0:
            continue
        else:
            t = False
            break
    return t


plik_liczby = open("liczby_przyklad.txt")
liczby = []
for x in plik_liczby.readlines():
    liczby.append(int(x.strip()))

for x in liczby:
    if x >= 100 and x <= 5000:
        if pierwsza(x):
            print(x)
