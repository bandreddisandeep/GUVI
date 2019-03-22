a=int(input())
b=1
n=2
while n<=a:
    if 2**b==a:
        b=0
        break
    else:
        n=2**b
        b=b+1
if(b!=0):
    b=b-2
    q=a-2**b
    print(q)
else:
    print(0)