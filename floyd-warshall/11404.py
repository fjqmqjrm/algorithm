# 11404 - 플로이드 (ok)
import sys
input = sys.stdin.readline
n = int(input()) # 도시
m = int(input()) # 버스
INF = sys.maxsize
disLi = [[INF]*(n+1)for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split()) # 출발도시, 도착도시, 필요비용
    if disLi[a][b] != [] and disLi[a][b] > c:
        disLi[a][b] = c
for i in range(1,n+1):
    disLi[i][i] = 0
for j in range(1,n+1):
    for k in range(1,n+1):
        for l in range(1,n+1):
            if k!= l and disLi[k][l] > disLi[k][j] + disLi[j][l]:
                disLi[k][l] = disLi[k][j] + disLi[j][l]

for i in range(1,n+1):
    for j in range(1,n+1):
        if disLi[i][j] == INF:
            print(0,end=" ")
        else:
            print(disLi[i][j],end=" ")
    print()

