# 11054 - 가장 긴 바이토닉 부분 수열 (ok)
import sys
input = sys.stdin.readline
N = int(input())
numArr = list(map(int,(input().split())))
# 1 5 2 1 4 3 4 5 2 1 -> 7
dp1 = [1]*200000
dp2 = [1]*200000
if N >= 2:
    for i in range(N):
        for j in range(i):
            if numArr[j] < numArr[i]:
                dp1[i] = max(dp1[i],dp1[j]+1)
    for i in range(N-1,-1,-1):
        for j in range(N-1,i,-1):
            if numArr[j] < numArr[i]:
                dp2[i] = max(dp2[i],dp2[j]+1)
dp = []
for i in range(N):
    dp.append(dp1[i]+dp2[i]-1)
print(max(dp))
