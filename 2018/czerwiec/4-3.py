plik1 = open("dane1.txt")
plik2 = open("dane2.txt")

dane1=[]
dane2=[]

for line in plik1.readlines():
    dane1.append(line.split())
for line in plik2.readlines():
    dane2.append(line.split())

counter = 0
for x in range(len(dane1)):
    liczby_dane1 = list(set(dane1[x]))
    liczby_dane2 = list(set(dane2[x]))
    liczby_dane1.sort()
    liczby_dane2.sort()
    if liczby_dane2 == liczby_dane1:
        print(liczby_dane1,liczby_dane2,x+1)
        counter+=1
print(counter)