import math
def wzor(xa,ya,xb,yb):
    return round(math.sqrt(pow((xb-xa),2)+pow((yb-ya),2)))

plik = open("punkty.txt")
y=[]
x=[]
dystans=[]

for c in plik.readlines():
    a = c.split()
    y.append(int(a[0]))
    x.append(int(a[1]))

for a in range(len(y)):
    for i in range(len(y)):
        dist=wzor(x[a],y[a],x[i],y[i])
        dystans.append(dist)

max_dystans = max(dystans)
print(max_dystans)