n=int(input())
r=input().split()
r1=[]
for i in  range(n):
    r1.append(int(r[i]))
r1.sort()

sumq=1
no=1
for j in range(len(r1)-1):
    if r1[j+1]>r1[j]:
        no=no+1
        sumq+=no
    else:
        sumq+=no
print(sumq)


