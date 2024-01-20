# 10773 - 제로 (ok)
import sys
input = sys.stdin.readline
N = int(input())


def add(li):
    tot = 0
    for i in li:
        tot += i
    return tot


numLi = []
for i in range(N):
    newNum = int(input())
    if newNum == 0:
        numLi.pop()
    else:
        numLi.append(newNum)
print(add(numLi))


