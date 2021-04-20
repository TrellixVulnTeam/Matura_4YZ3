plik = open("dane_6_2.txt")
tab = []
nowe_slowa = []

def zaszyfruj(slowo,k):
    nowe_slowo=""
    for litera in slowo:
        nowe_slowo += chr(((ord(litera) - 65 + k) % 26) + 65)
    return nowe_slowo

for line in plik.readlines():
    s=line.split()
    print(zaszyfruj(s[0],-int(s[1])))
