n=input().split()
a=int(n[0])
b=int(n[1])
s=[]
for i in range(a+1,b):
    if i%2==0:
        s.append(i)
for j in range(len(s)-1):
    print(s[j],end=" ")
print(s[-1],end="")

