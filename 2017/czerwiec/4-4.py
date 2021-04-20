plik = open("punkty.txt")
y=[]
x=[]
counterA=0
counterB=0
counterC=0
for c in plik.readlines():
    a = c.split()
    y.append(int(a[0]))
    x.append(int(a[1]))

for a in range(len(x)):
    if x[a]<5000 and x[a]> -5000 and y[a]> -5000 and y[a]<5000:
        counterA+=1
    if x[a]==5000 or x[a]== -5000 or y[a]==5000 or y[a]== -5000:
        counterB+=1
    if x[a]>5000 or x[a]< -5000 or y[a]< -5000 or y[a]>5000:
        counterC+=1

print("A ",counterA)
print("B ",counterB)
print("C ",counterC)
