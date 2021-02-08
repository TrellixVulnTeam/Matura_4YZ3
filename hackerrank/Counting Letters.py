"""
In this task you have to count the letters (a-zA-Z) in a sentence and write the letter that appeared the most number of time. If there are several such letters, print the one that is first in the alphabet. The sentence can contain other characters.

Sample Input 0

some sentence.
Sample Output 0

e
Explanation 0

'e' appearde 4 times, which is the most.

Sample Input 1

---a---
Sample Output 1

a
Sample Input 2

aacccAA
Sample Output 2

a
"""
import string
alf = input()
alf = alf.lower()
alf = list(alf)
alf.sort(reverse=True)
suma, new_suma = 0, 0
litera = ""
for x in range(len(alf)):
    if (alf[x] not in string.ascii_lowercase):
        break
    else:
        suma = alf.count(alf[x])
        if suma >= new_suma:
            new_suma = suma
            litera = alf[x]
print(litera,new_suma)
