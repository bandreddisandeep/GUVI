a='dhoni'
b=['d','h','o','n','i']
c=input().lower()
d=list(c)
flag=0

for i in range(len(b)):
    if b[i] not in d:
        flag=1
        
if c==a or flag==1:
    print('no')
else:
    print('yes')
    

