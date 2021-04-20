plik_pierwsze = open("pierwsze_przyklad.txt")
pierwsze = []
lista = []
for y in plik_pierwsze.readlines():
    pierwsze.append(int(y.strip()))


def rozklad(x):
    tab = []
    while x != 0:
        temp = x % 10
        x = x // 10
        tab.append(temp)
    tab.reverse()
    return tab


for x in pierwsze:
    while len(str(x))!=1:
        x = sum(rozklad(x))
        rozklad(x)
    lista.append(x)

print(lista.count(1))