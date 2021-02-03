dane = open("dane.txt", "r")
liczby = dane.readline()
liczby = liczby.split(";")
porowanie = open("porownanie.txt", "r")
liczby_porownanie = porowanie.readline()
liczby_porownanie = liczby_porownanie.split(";")

# print(liczby)

for x in range(len(liczby)):
    liczby[x] = int(liczby[x])

# print(liczby_porowanie)

for x in range(len(liczby_porownanie)):
    liczby_porownanie[x] = int(liczby_porownanie[x])

liczby_porownanie.append(11)
print(liczby)
print(liczby_porownanie)

for x in liczby:
    if x not in liczby_porownanie:
        print(x)

for x in liczby_porownanie:
    if x not in liczby:
        print(x)

