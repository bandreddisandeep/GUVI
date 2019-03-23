n=int(input())
a=input().split()
a1=[]
a2=[]
for i in range(n):
    a1.append(int(a[i]))

for j in range(n):
    if j==a1[j]:
        a2.append(j)
if len(a2)!=0:
    for k in range(len(a2)):
        print(a2[k])
else:
    print(-1)
        

