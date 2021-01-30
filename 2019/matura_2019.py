import math

def drugi(a):
    cyfry = []
    tmp = a
    while tmp > 0:
        cyfry.append(tmp%10)
        tmp //= 10
    suma = 0
    for i in cyfry:
        suma += math.factorial(i)
    return suma == a

tab = []
with open("przyklad.txt") as file:
    for line in file.readlines():
        tab.append(int(line))

ans1 = 0

trojki = [3**x for x in range(7)]#wszystkie potegi trojki

for element in trojki:
    print(element)

print()

for element in tab:
    if element in trojki:
        ans1 += 1

print("zadanie 1 ",ans1)

ans2 = 0

for element in tab:
    if drugi(element):
        ans2 += 1
print("zadanie 2 ",ans2)