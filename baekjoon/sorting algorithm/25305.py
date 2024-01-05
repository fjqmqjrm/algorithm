# 25305 - 커트라인
N, k = map(int,input().split())
numLi = list(map(int,input().split()))
numLi.sort()
print(numLi[N-k]) 