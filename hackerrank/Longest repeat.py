n = input()
litera = ''
length = 1
last_char = n[0]
counter = 1
for i in range(1, len(n)):
    if counter > length:
        length = counter
        litera = n[i - 1]
    if n[i] == last_char:
        counter += 1
    else:
        counter = 1
    last_char = n[i]

print(litera)