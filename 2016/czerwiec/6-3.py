plik = open("liczby.txt")
tab = []
dwojkowo = []
dziesietnie = []
counter = 0
for x in plik.readlines():
    tab.append(x.strip())

for liczba in tab:
    if (liczba[len(liczba)-1] == "2"):
        dwojkowo.append(liczba[:len(liczba)-1])
for x in dwojkowo:
    dziesietnie.append((int(x,2)))
for x in dziesietnie:
    if x %2 == 0:
        counter+=1
print(counter)