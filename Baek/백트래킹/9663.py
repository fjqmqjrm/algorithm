from collections import deque
N = int(input())

vCol = [0]*N
vMin = [0]*(2*N-1)
vMax = [0]*(2*N-1)
answer = 0
def dfs(n):
    global answer

    if n == N:
        answer += 1
        return

    for j in range(N):
        if vCol[j] == vMax[j+n] == vMin[n-j] == 0:
            vCol[j] = vMax[j+n] = vMin[n-j] = 1
            dfs(n+1)
            vCol[j] = vMax[j+n] = vMin[n-j] = 0



dfs(0)
print(answer)