a2='dhoni'
b2=['d','h','o','n','i']
c2=input().lower()
d2=list(c2)
fl=0

for j in range(len(b2)):
    if b2[j] not in d2:
        fl=1
        
for k in range(len(c2)):
    if c2[k] not in b2:
        fl=1
        
if c2==a2 or fl==1:
    print('no')
else:
    print('yes')
    

