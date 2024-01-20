# 9663 - N-Queen (아직 못 품)
# 행이 다르고&열이 다르고&열-행이 다르고
import sys
input = sys.stdin.readline
N = int(input())
row = [_ for _ in range(1,N+1)]
col = [_ for _ in range(1,N+1)]
tot = N*N
count = 0
rc = [False] * N
cc = [False] * N
ans = []
def back_t(ans,row,col):
    global count
    if len(ans) == N:
        count += 1
        return 
    else:
        for r in range (len(row)):
            if rc[r] == False:
                rc[r] = True
                que = [row[r]]
            for c in range (len(col)):
                if cc[c] == False:
                    cc[c] = True
                    que.append(col[c])





print(col)

