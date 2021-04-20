plik = open("dane_6_1.txt")
tab = []
nowe_slowa = []
for x in plik.readlines():
    tab.append(x.strip())

def zaszyfruj(slowo,k):
    nowe_slowo=""
    for litera in slowo:
        nowe_slowo += chr(((ord(litera) - 65 + k) % 26) + 65)
    return nowe_slowo

#print(zaszyfruj("INTERPRETOWANIE ",107))


for litera in tab:
    nowe_slowa.append(zaszyfruj(litera,107))
print(nowe_slowa)
print(zaszyfruj("ZAWISLAK",12))