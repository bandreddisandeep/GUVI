a=input().split()
c=int(a[0])
for i in range(1,len(a)):
    if c>int(a[i]):
        c=c
    else:
        c=int(a[i])
print(c)


