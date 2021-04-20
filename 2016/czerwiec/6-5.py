plik = open("liczby.txt")
tab = []
systemy = []
dziesietnie = []
for x in plik.readlines():
    tab.append(x.strip())
for x in tab:
    systemy.append(((x[-1])))

for liczba in tab:
    if (liczba[len(liczba)-1] == "6"):
        liczba = liczba[:len(liczba)-1]
        dziesietnie.append(int(liczba,6))
    else:
        if (liczba[len(liczba)-1] == "2"):
            liczba = liczba[:len(liczba) - 1]
            dziesietnie.append(int(liczba, 2))
        else:
            if (liczba[len(liczba)-1] == "8"):
                liczba = liczba[:len(liczba) - 1]
                dziesietnie.append(int(liczba, 8))
            else:
                if (liczba[len(liczba)-1] == "9"):
                    liczba = liczba[:len(liczba) - 1]
                    dziesietnie.append(int(liczba, 9))
                else:
                    if (liczba[len(liczba)-1] == "3"):
                        liczba = liczba[:len(liczba) - 1]
                        dziesietnie.append(int(liczba, 3))
                    else:
                        if (liczba[len(liczba)-1] == "7"):
                            liczba = liczba[:len(liczba) - 1]
                            dziesietnie.append(int(liczba, 7))
                        else:
                            if (liczba[len(liczba)-1] == "4"):
                                liczba = liczba[:len(liczba) - 1]
                                dziesietnie.append(int(liczba, 4))
                            else:
                                if (liczba[len(liczba)-1] == "5"):
                                    liczba = liczba[:len(liczba) - 1]
                                    dziesietnie.append(int(liczba, 5))
print(min(dziesietnie),max(dziesietnie))
print(tab[dziesietnie.index(min(dziesietnie))],tab[dziesietnie.index(max(dziesietnie))])