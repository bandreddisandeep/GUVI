x=input().split()
i=int(x[0])
a=int(x[1])
suma=0
if i>=a:
    y=input().split()
    for j in range(a):
        suma+=int(y[j])
    print(suma)
else:
    print('invalid')
