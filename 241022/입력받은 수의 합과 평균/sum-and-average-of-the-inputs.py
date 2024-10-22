n = int(input())
sum =0
for i in range(n):
    k=int(input())
    sum += k

avg = sum/n
print(f"{sum} {avg:.1f}")