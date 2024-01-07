n, k = map(int,input().split())
moneys=[]
result = 0

for i in range(n):
    moneys.append(int(input()))
if n == 1:
    result += k//moneys[0]
    print(result)
    exit(0)

for i in range(n-1,-1,-1):
    if k == 0:
        break

    if k - moneys[i] < 0:
        continue
    else:
        result += k // moneys[i]
        k = k%moneys[i]

print(result)