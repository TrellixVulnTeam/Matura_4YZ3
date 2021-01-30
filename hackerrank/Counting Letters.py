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
x = input("Enter sentance")
tab = []
ans = 0
for i in range(len(x)):
    tab.append(x[i])
for i in range(len(x)):
    if (x[0] == tab[i]):
         ans += 1

