# 1010 - 다리 놓기 (ok)
import sys
input = sys.stdin.readline
T = int(input())
li = [[]for i in range(T)]
for i in range(T):
    a,b = map(int,input().split())
    li[i] = (a,b)

for i in range(T):
    minNum = min(li[i])
    maxNum = max(li[i])
    #maxCmin
    maxtot = 1
    for i in range(minNum):
        maxtot *= maxNum
        maxNum -= 1
    mintot = 1
    for i in range(1,minNum+1):
        mintot *= i

    print(maxtot//mintot)