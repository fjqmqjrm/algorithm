# 18870 - 좌표 압축
# bisect(이진 탐색)라이브러리를 통한 시간복잡도 해결(이미 정렬된 리스트)
import bisect
from sys import stdin
N = int(stdin.readline())
numLi = list(map(int,stdin.readline().split()))
copyLi = sorted(list(set(numLi)))
for i in range(N):
    print(bisect.bisect_left(copyLi,numLi[i]), end = " ")
