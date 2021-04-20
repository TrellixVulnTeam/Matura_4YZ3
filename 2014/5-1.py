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

plik = open("NAPIS.TXT")
slowa=[]
asci=[]
counter=0
for line in plik.readlines():
    slowa.append(line.strip())
for slowo in slowa:
    suma=0
    for litera in slowo:
        suma+=ord(litera)
    asci.append(suma)

for element in asci:
    if pierwsza(element):
        counter+=1

print(counter)