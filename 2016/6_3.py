plik = open("dane_6_2.txt")

slowa1 = []
slowa2 = []

for line in plik.readlines():
    s=line.split()
    slowa1.append(s[0])
    slowa2.append(s[1])

