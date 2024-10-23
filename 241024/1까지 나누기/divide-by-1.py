n = int(input())

i=1
while n%i <=1:
    n //= i
    i += 1
    continue

print(i)