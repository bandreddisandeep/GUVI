q=int(input())
x=input().split()
l=[]
i1=[]
def no(n):
    m=0
    while n>0:
        if n%2==1:
            m=m+1
        n=n//2
    i1.append(m)
for i in range(q):
    l.append(int(x[i]))
for j in range(q):
    no(l[j])
f=[]
for k in range(q):
    w=[]
    w.append(i1[k])
    w.append(l[k])
    f.append(w)
f.sort()
for p in range(len(f)-1,-1,-1):
    print(f[p][1])

    