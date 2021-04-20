plik = open("NAPIS.TXT")
slowa=[]
asci=[]
ros=[]
for line in plik.readlines():
    slowa.append(line.strip())
for slowo in slowa:
    ans = 1
    for x in range(1,len(slowo)):
        if slowo[x]>slowo[x-1]:
            continue
        else:
            ans = 0
    if ans:
        print(slowo)
            