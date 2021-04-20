file = open("NAPIS.TXT")
slowa=[]

for line in file.readlines():
    slowa.append(line.strip())

zuzyte=[]
for wyraz in slowa:
    if wyraz not in zuzyte:
        a=slowa.count(wyraz)
        zuzyte.append(wyraz)
        if a > 1:
            print(wyraz)