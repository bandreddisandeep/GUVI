n=int(input())
a=input().split()
a1=[]
a2=[]
for i in range(n):
    a1.append(a[i])
a1.sort()
for j in range(n-1,-1,-1):
    a2.append(a1[j])
st="->"
a2=st.join(a2)
print(a2)