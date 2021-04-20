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
plik = open("punkty.txt")
tab=[]
liczby=[]
b=[]
y=[]
x=[]
counter=0
for c in plik.readlines():
    a = c.split()
    y.append(int(a[0]))
    x.append(int(a[1]))

for i in range(len(y)):
    if pierwsza(y[i]) and pierwsza(x[i]):
        counter+=1
print(counter)