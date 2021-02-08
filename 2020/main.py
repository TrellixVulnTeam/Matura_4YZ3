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
plik = open("przyklad.txt", "r")
liczby = []
znaki = []
parzyste = []
pierwsza2 = []
for line in plik.readlines():
    a = line.split()
    liczby.append(int(a[0]))
    znaki.append(a[1])
for x in liczby:
    if x > 4 and x % 2 == 0:
        parzyste.append(x)
for x in range(3, max(parzyste)):
    if pierwsza(x) == True:
        pierwsza2.append(x)
roznica = 0
for x in range(len(parzyste)):
    for i in range(len(pierwsza2)):
        roznica = parzyste[x] - pierwsza2[i]
        if roznica in pierwsza2:
            print(parzyste[x], "=", pierwsza2[i], "+", roznica)
            break
znaki = list(znaki)
for element in znaki:
    new_counter = -1
    old_counter = 0
    old_letter = ""
    new_letter = ""
    for i in element:
        if old_letter == i:
            old_counter += 1
        else:
            if new_counter < old_counter:
                new_counter = old_counter
                new_letter = old_letter
            old_counter = 1
            old_letter = i
    print(element,new_letter*new_counter,new_counter)
def sprawdzenie(liczby,znaki):
    mniejsze=[]
    nowa_liczby = []
    nowa_znaki = []
    for x in range(len(liczby)):
        if x + 1 < len(liczby):
            if liczby[x] != liczby[x + 1]:
                if liczby[x] > liczby[x + 1]:
                    mniejsze.append(x)
                else:
                    mniejsze.append(x+1)
            else:
                if znaki[x]!=znaki[x+1]:
                    if znaki[x]>znaki[x+1]:
                        mniejsze.append(x)
                    else:
                        mniejsze.append(x+1)
                else:
                    mniejsze.append(x+1)
        else:
            break
    mniejsze=list(set(mniejsze))
    for x in range(len(znaki)):
        if x not in mniejsze:
            nowa_liczby.append(liczby[x])
            nowa_znaki.append(znaki[x])
    return nowa_liczby+nowa_znaki
l1=[]
l2=[]
for i in range(len(sprawdzenie(liczby,znaki))):
    if i<len(sprawdzenie(liczby,znaki))//2:
        l1.append(sprawdzenie(liczby,znaki)[i])
    else:
        l2.append(sprawdzenie(liczby, znaki)[i])
print(*sprawdzenie(l1,l2))
