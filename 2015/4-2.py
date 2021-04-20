plik = open("liczby.txt")
tab=[]
dwojki=0
osemki=0
for x in plik.readlines():
    tab.append(int(x.strip(),2))
for element in tab:
    if element%2==0:
        dwojki+=1
    if element%8==0:
        osemki+=1
print("dwojki ",dwojki,"osemki",osemki)
