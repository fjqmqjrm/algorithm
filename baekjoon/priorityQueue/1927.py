# 1927 - 최소 힙 (ok)
import heapq, sys
input = sys.stdin.readline
N = int(input())
minHeap = []
prinLi = []
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(minHeap, x)
    else:
        if len(minHeap) == 0:
            prinLi.append(0)
        else:
            prinLi.append(heapq.heappop(minHeap))
for i in prinLi:
    print(i)