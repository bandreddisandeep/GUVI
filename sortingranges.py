k=int(input())
b=[]
for i in range(k):
    a=[]
    a=input().split()
    for  j in range(len(a)):
        b.append(int(a[j]))
b.sort()
for t in range(len(b)-1):
    print(b[t],end=" ")
print(b[-1])