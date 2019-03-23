n=input().split()
n1=int(n[0])
n2=int(n[1])
x=input().split()
x1=[]
for i in range(n1):
    x1.append(int(x[i]))
fl=0
for j in range(n1-1):
    for k in range(j+1,n1):
        if x1[j]+x1[k]==n2:
            fl=1
if fl==1:
    print('yes')
else:
    print('no')

