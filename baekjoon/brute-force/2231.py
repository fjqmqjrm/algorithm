# 2231 - 분해합 (20240102) ok
N = int(input())
i = 1
min = N
while True:
    if i == N:
        break
    num = i
    num = str(num)
    hap = i
    for k in num :
        hap += int(k)
    if hap == N :
        if min > i:
            min = i
    i += 1
if min == N:
    print(0)
else:
    print(min)