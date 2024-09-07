a=input().split()
b=input().split()
c=input().split()

sym1,tem1=a[0], int(a[1])
sym2,tem2=b[0], int(b[1])
sym3,tem3=c[0], int(c[1])

totalA=0

if sym1=="Y" and tem1>=37:
    totalA += 1

if sym2=="Y" and tem2>=37:
    totalA += 1

if sym3=="Y" and tem3>=37:
    totalA += 1

if totalA>=2:
    print("E")
else:
    print("N")