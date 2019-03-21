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
    if a[i] in ['1','2','3','4','5','6','7','8','9','0']:
        if a[i] in b:
            b.remove(a[i])
    
    elif a[i]!=b[i]:
        break
    else:
        c.append(a[i])
    
print(len(b)-len(c))
    
