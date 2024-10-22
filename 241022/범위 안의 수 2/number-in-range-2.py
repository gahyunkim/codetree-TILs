sum, cnt =0,0
for _ in range(10):
    n = int(input())
    if n>=0 and n<=200:
        sum+= n
        cnt +=1

avg = sum/cnt
print(f"{sum} {avg:.1f}")