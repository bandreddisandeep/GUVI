a=int(input())
b=input().split()
b1=[]
for i in range(a):
    b1.append(b[i])
sums=0
for i in  range(1,len(b1)):
    for j in range(i):
        if int(b1[j])<int(b1[i]):
            sums=sums+int(b1[j])
        else:
            sums+=0
print(sums)