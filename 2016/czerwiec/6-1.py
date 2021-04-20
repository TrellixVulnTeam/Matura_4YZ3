plik = open("liczby.txt")
tab = []
counter = 0
for x in plik.readlines():
    tab.append(x.strip())

for liczba in tab:
    if (liczba[len(liczba)-1]) == "8":
        counter +=1
print(counter)