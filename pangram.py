x=input().split()
y=[]
flag=0
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(x)):
    for j in range(len(x[i])):
        y.append(x[i][j].lower())

for j in range(len(a)):
    if a[j] not in y:
        flag=1
        
if flag==0:
    print('yes')
else:
    print('no')
    