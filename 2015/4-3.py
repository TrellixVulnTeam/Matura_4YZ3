plik = open("liczby.txt")
tab=[]
counter=0
for x in plik.readlines():
    tab.append(int(x.strip(),2))
min = min(tab)
max = max(tab)

print(tab.index(min)+1,tab.index(max)+1)