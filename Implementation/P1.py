# 상하좌우 문제
# 여행가 A는 NxN 정사각형 공간 위에 있습니다. 이 공간은 1x1 크기의 정사각형으로 나누어져 있습니다
# 여행가 A는 상 하 좌 우 방향으로 이동할 수 있으며 시작 좌표하는 항상 (1,1) 입니다
# 우리 앞에는 여행가 A가 이동할 계획서가 놓여져 있습니다.
# 각 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하며 L,R,U,D 중 하나의 문자가 반복적으로 적혀있습니다.
# L : 왼쪽 한칸 이동 R : 오른쪽 한칸 이동 U : 위로 한칸 이동 D : 아래로 한칸 이동
# 이 때 공간을 벗어나는 움직임은 무시합니다.
# 이동 후의 위치를 알아내는 프로그램을 작성하시오

n = int(input())
direction = input().split()

option = ['L','R','U','D']
dy = [-1, 1, 0,0]
dx = [0,0,1,-1]

x = 1
y = 1

for d in direction:
    for i in range(len(option)):
        if d == option[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx>n or nx<1 or ny>n or ny < 1:
        continue
    x = nx
    y = ny

print(x,y)