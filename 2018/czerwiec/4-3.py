plik1 = open("dane1.txt")
plik2 = open("dane2.txt")

dane1=[]
dane2=[]
dane1_ostatnie=[]
dane2_ostatnie=[]
counter=0

for line in plik1.readlines():
    dane1.append(line.split())
for line in plik2.readlines():
    dane2.append(line.split())