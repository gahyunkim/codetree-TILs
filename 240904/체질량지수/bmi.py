arr=input().split()
h,w=int(arr[0]),int(arr[1])
bmi=(10000*w)//(h*h)

print(bmi)
if bmi>=25:
    print("Obesity")