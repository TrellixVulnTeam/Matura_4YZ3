piksele=[]
file = open("dane.txt")
for line in file.readlines():
    piksele.append(line.split())

def rzad(tablica,x):
    for y in range(200):
        liczba = (tablica[y][x])
        print(liczba)


for x in range(320):
    rzad(piksele,x)