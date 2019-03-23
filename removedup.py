i=list(input())
a=[]
for j in range(len(i)):
    if i[j] not in a:
        a.append(i[j])
str=""
a=str.join(a)
print(a)
        