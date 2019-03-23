n=input().split()
a=int(n[0])
b=int(n[1])
s=[]
for i in range(a+1,b):
    if i%2==0:
        s.append(i)
        
if len(s)==1:
    print(s[0])
else:
        
    for j in range(0,len(s)-1):
        print(s[j],end=" ")
    print(s[-1],end="")


