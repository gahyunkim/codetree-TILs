arr=input().split()
a,b,c=int(arr[0]),int(arr[1]),int(arr[2])

if a<=b and a<=c:
    d=a 
elif b<=a and b<=c:
    d=b
else:
    d=c

print(d)