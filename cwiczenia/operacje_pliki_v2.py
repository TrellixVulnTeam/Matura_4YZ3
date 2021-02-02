def is_prime(n):
    t = True
    if n == 1:
        return False
    for x in range(2, int(n**(1/2)+1)):
        if n%x !=0:
            continue
        else:
            t = False
            break

    return t

n=int(input())
la=[]
lb=[]
with open("notatnik.txt") as plik:
    for x in range(n):
        line = plik.readline()
        la.append(int(line))
print(la)

for i in la:
    if is_prime(i):
        print(i)
        lb.append(i)
print(lb)