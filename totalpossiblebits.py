q=int(input())
x=[]
for i in range(2**q):
    x.append(i)
l=[]
i1=[]
def no(n):
    m=0
    while n>0:
        if n%2==1:
            m=m+1
        n=n//2
    i1.append(m)

for j in range(len(x)):
    no(x[j])
f=[]
for k in range(len(x)):
    w=[]
    w.append(i1[k])
    w.append(x[k])
    f.append(w)
f.sort()
for p in range(len(f)):
    l.append(f[p][1])
    

c=[]
for i in range(len(x)):
    b=[]
    l1=l[i]
    for j in range(q):
        a=l1%2
        b.append(a)
        l1=l1//2
    b.reverse()
    c.append(b)

for f in range(len(c)):
    for d in range(q-1):
        print(c[f][d],end=" ")
    print(c[f][-1])
    
    

    