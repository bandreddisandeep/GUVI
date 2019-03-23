n=int(input())
a=input().split()
a1=[]
for i in range(n):
    a1.append(int(a[i]))

for j in range(n):
    if j==a1[j]:
        print(j , end=" ")

