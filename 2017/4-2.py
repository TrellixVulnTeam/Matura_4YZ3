file = open("dane.txt")
dane=[]
liczby=[]
counter=0
for line in file.readlines():
    dane=line.split()
    for i in range(len(dane)//2):
        if(dane[i]==dane[len(dane)-1-i]):
            continue
        else:
            counter+=1
            break

print(counter)
