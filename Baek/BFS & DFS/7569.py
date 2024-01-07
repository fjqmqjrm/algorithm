"""
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다."""
from collections import deque
m,n,h = map(int,input().split())

q = deque()
appleq = []
graph = []
cnt = 0
for i in range(h):
    data=[]
    for j in range(n):
        d = list(map(int, input().split()))
        for k in range(m):
            if d[k] == 0:
                appleq.append((k,j,i))
            if d[k] == 1:
                q.append((k,j,i))
            if d[k] == 1 or d[k]==-1:
                cnt+=1
        data.append(d)
    graph.append(data)

if cnt == m*n*h:
    print(0)
    exit(0)

day = 0
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():

    global day

    nextq = deque()

    while True:
        while q:
            x,y,z = q.popleft()
            graph[z][y][x] = 2
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if nx >=m or nx <0 or ny >=n or ny<0 or nz >=h or nz <0:
                    continue
                if graph[nz][ny][nx] == -1:
                    continue
                if graph[nz][ny][nx] == 1:
                    q.append((nx,ny,nz))
                    continue
                if graph[nz][ny][nx] == 0:
                    nextq.append((nx,ny,nz))
                    if appleq.count((nx,ny,nz))!=0:
                        appleq.remove((nx, ny, nz))
                    continue
        if len(nextq) == 0:
            break

        while nextq:
            x,y,z = nextq.popleft()
            graph[z][y][x] = 1
            q.append((x,y,z))

        day+=1


bfs()
if len(appleq) != 0:
    print(-1)
    exit(0)
print(day)
