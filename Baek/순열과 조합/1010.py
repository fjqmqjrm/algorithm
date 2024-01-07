from math import factorial
tc = int(input())
result = []
for t in range(tc):
    n, m = map(int,input().split())
    bridge = int(factorial(m) // (factorial(n) * factorial(m-n)))
    result.append(bridge)

for i in result:
    print(i)