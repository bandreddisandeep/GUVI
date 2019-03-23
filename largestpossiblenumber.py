n=int(input())
x=input().split()
x1=[]
for i in range(n):
    x1.append(int(x[i]))
x1.sort()
t=0
for j in range(len(x1)):
    s=x1[j]*(10**j)
    t=t+s
print(t)