n = int(input())
reszta = []
while n > 0:
    reszta.append(n % 2)
    n //= 2
reszta.reverse()
print(*reszta)
