input1=input()
arr=input1.split()

input2=input()
brr=input2.split()

a,b,c,d=int(arr[0]),int(arr[1]),int(brr[0]), int(brr[1])

if a>c:
    print("A")
elif a==c and b>d:
    print("A")
else:
    print("B")