n=input().split()
n1=int(n[0])
n2=int(n[1])
x=input().split()
x1=[]
for i in range(n1):
    x1.append(int(x[i]))
x1.sort()
print(x1[-n2])