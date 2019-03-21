x=input().split()
y=list(x[0])
z=list(x[1])
c=[]
if len(y)<len(z):
    a=y
    b=z
else:
    a=z
    b=y

for i in range(len(a)):
    k=j=0
    if a[i]!=b[i]:
        break
    else:
        c.append(a[i])
    
print(len(b)-len(c))
    