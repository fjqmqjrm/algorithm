# 미로 탈출 문제
# 동빈이는 N x M 미로에 갇혔습니다. 미로에는 여러마리 괴물이 있어 이를 피해 탈출해야합니다.
# 동빈이의 위치는 (1,1) 이며 미로의 출구는 (N,M)에 존재합니다
# 괴물이 존재하는 위치는 0으로 괴물이 없는 위치는 1로 표시됩니다.
# 이때 탈출할 때 움직이는 칸의 최소한을 구하는 프로그램을 짜시오. 단 시작과 끝도 포함하여 계산합니다.
from collections import deque

distance = []

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx >=n or nx <0 or ny >= m or ny <0:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] =graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1]



n ,m= map(int, input().split())
graph = []
result = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    graph.append(list(map(int,input())))

print(bfs(0,0))


