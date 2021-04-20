plik = open("liczby.txt")
tab = []
osemkowe = []
dziesietne = []
for x in plik.readlines():
    tab.append(x.strip())
for liczba in tab:
    if (liczba[len(liczba)-1] == "8"):
       osemkowe.append(liczba[:len(liczba)-1])
for x in osemkowe:
    dziesietne.append(int(x,8))
print(sum(dziesietne))