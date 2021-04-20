def rozklad(n):
    a = list(set(n))
    a.sort()
    return a

plik = open("punkty.txt")
y=[]
x=[]
counter=0
for c in plik.readlines():
    a = c.split()
    y.append(a[0])
    x.append(a[1])

for z in range(len(x)):
     if rozklad(y[z]) == rozklad(x[z]):
         counter+=1


print(counter)