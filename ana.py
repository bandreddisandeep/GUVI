a1='dhoni'
b1=['d','h','o','n','i']
c1=input().lower()
d1=list(c1)
fla=0

for j in range(len(b1)):
    if b1[j] not in d1:
        fla=1
        
for k in range(len(c)):
    if c[k] not in b:
        fla=1
        
if c1==a1 or fla==1:
    print('no')
else:
    print('yes')
    

