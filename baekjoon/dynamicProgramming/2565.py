# 2565 - 전깃줄 (ok)
import sys
input = sys.stdin.readline
N = int(input())
lineDp = [1] * 1000
line = []
for i in range(N):
    a,b = map(int,input().split())
    line.append([a,b])
line = sorted(line)
for i in range(len(line)):
    for j in range(i):
        if line[i][1] >= line[j][1]:
            lineDp[i] = max(lineDp[j]+1,lineDp[i])
print(N-max(lineDp))


