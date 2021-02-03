n=int(input())
la=[]
lb={}
for x in range(n):
    a=int(input())
    la.append(a)
print(la)
counter=0
for i in range(1,len(la)):
    for j in range(1,len(la)):
        if i+1==len(la):
            break
        else:
            counter+=1
            if la[i+1]>=j:
                lb[i]=counter
print(lb)

