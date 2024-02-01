# 9251 - LCS
import sys
#from collections import deque
input = sys.stdin.readline
a = list(input())
a.pop()
b = list(input())
b.pop()
dp = [[0 for i in range(len(a)+1)]for j in range(len(b)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[j+1][i+1] = dp[j][i] + 1
        else:
            dp[j+1][i+1] = max(dp[j][i+1],dp[j+1][i])
print(dp[len(b)][len(a)])

