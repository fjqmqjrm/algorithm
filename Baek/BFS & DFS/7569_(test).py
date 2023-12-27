from collections import deque

m,n,h = map(int,input().split())
day = 0
count = m*n*h
tomatoes = [
    [list(map(int,input().split())) for i in range(n)]in range(h)
]



dz = [0,0,1,-1,0,0]
dx = [1,-1,0,0,0,0]
dy = [0,0,0,0,1,-1]

def func(x,y,z,cond):
    global day
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx>=m or nx < 0 or ny >= n or ny <0 or nz >=h or nz<0:
            continue
        if tomatoes[nz][nx][ny] == 0:
            tomatoes[nz][nx][ny] = 1
        else:
            continue

