piksele=[]
file = open("dane.txt")
liczby=[]
for line in file.readlines():
    piksele=piksele+line.split()

for element in piksele:
    element=int(element)
    liczby.append(element)
print(max(liczby),min(liczby))