def sumw(l,r):
    su=0
    g=[]
    for i in range(l-1,r):
        g.append(int(a[i]))        
    for j in range(len(g)):
        su=su+g[j]
            
    print(su)
    

s=input().split()
n=int(s[0])
q=int(s[1])
b1=[]

a=[]
A=input().split()
for l in range(n):
    a.append(A[l])
for p in range(q):
    b=input().split()
    b1.append(b)
for u in  range(q):
    if b1[u][0]==b1[u][1]:
        f=int(b1[u][0])
        print(a[f-1])
    else:
        l=int(b1[u][0])
        r=int(b1[u][1])
        sumw(l,r)