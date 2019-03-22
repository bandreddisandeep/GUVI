a=input().split()
b=int(a[0])
c=int(a[1])
d=int(a[2])
if b%2==0:
    b1=b//2
    c1=c+d
    d1=b//c1
    
    f=0
    for i in range(d1+1):
        if (c*i+d*i)==b1:
            f=1
    if f==0:
        print('NO')
    else:
        print('YES')
else:
    print('NO')

