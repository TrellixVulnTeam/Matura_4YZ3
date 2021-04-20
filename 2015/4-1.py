plik = open("liczby.txt")
tab=[]
counter=0
for x in plik.readlines():
    tab.append(str(x.strip()))
for element in tab:
    zero = element.count("0")
    one = element.count("1")
    if zero > one:
        counter+=1
print(counter)