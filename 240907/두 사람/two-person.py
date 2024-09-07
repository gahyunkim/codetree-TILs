arr=input().split()
brr=input().split()

a,b,c,d=int(arr[0]),arr[1], int(brr[0]),brr[1]

if (a>=19 and b=="M") or (c>=19 and d=="M"):
    print(1)
else:
    print(0)