def pierwsza(n):
    t = True
    if n == 1:
        return False
    for x in range(2, int(n ** (1 / 2) + 1)):
        if n % x != 0:
            continue
        else:
            t = False
            break
    return t

plik_pierwsze = open("pierwsze_przyklad.txt")
pierwsze = []

for y in plik_pierwsze.readlines():
    pierwsze.append(y.strip())

for x in pierwsze:
   if pierwsza(int(x[::-1])):
       print(x)