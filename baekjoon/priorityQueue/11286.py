# 11286 - 절댓값 힙 (ok)
import heapq, sys
input = sys.stdin.readline
N = int(input())
pMinHeap = [] # 양수 최소 힙
mMinHeap = [] # 음수 절댓값 최소 힙
prinLi = []
for i in range(N):
    x = int(input())
    if x < 0 :
        heapq.heappush(mMinHeap,-x)
    elif x > 0:
        heapq.heappush(pMinHeap,x)
    #[-1,-2,-3..] [1,3,4..]
    else:
        if len(mMinHeap) == 0 and len(pMinHeap) == 0:
            prinLi.append(0)
        elif len(mMinHeap) == 0:
            prinLi.append(heapq.heappop(pMinHeap))
        elif len(pMinHeap) == 0:
            prinLi.append(-(heapq.heappop(mMinHeap)))
        else:
            if mMinHeap[0] <= pMinHeap[0]:
                prinLi.append(-(heapq.heappop(mMinHeap)))
            elif mMinHeap[0] > pMinHeap[0]:
                prinLi.append(heapq.heappop(pMinHeap))

for i in prinLi:
    print(i)
