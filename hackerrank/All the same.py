z = int(input("Enter n "))
tab = []
for i in range(z):
    tab.append(input("Enter List "))
    print(tab[i])

result = all(element == tab[0] for element in tab)
if result:
    print("True")
else:
    print("False")

print(tab)
