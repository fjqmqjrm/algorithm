# 11279 - 최대 힙 (ok)
import heapq,sys
input = sys.stdin.readline
N = int(input())
heap = []
prinLi = []
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, -x)
    else:
        if len(heap) == 0:
            prinLi.append(0)
        else:
            prinLi.append(-(heapq.heappop(heap)))

for i in prinLi:
    print(i)


