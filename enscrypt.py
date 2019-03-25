a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i1=list(input())
i2=list(input())
i1n=[]
i2n=[]
ixn=[]
for i in range(len(i1)):
    for j in range(len(a)):
        if i1[i]==a[j]:
            i1n.append(j+1)
for k in range(len(i2)):
    for l in range(len(a)):
        if i2[k]==a[l]:
            i2n.append(l+1)


for i in range(len(i1)):
    x=i1n[i]+i2n[i]
    x=x%26
    ixn.append(x)
final=[]
for i in range(len(i1)):
    g=a[ixn[i]-1]
    final.append(g)

final=''.join(final)
print(final)

