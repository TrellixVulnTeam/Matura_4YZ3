n=int(input())
li=[]
l2=[]
file = open("notatnik.txt")
for line in file.readlines():
    #line=list(file.readline(n))
    li.append(line)

print(li)

file2=open("wynik.txt","w")

for x in range(len(li)):
    a=li[x]
    a=a[:n]
    l2.append(a)
    file2.write(l2[x]+"\n")
print(l2)
file.close()