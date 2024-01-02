# 음료수 얼려 먹기 - 닫힌 공간 세는 개념
n, m = map(int, input().split())

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상 , 하 , 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1) # 더 이상 호출할 곳이 없으면 True반환
        return True
    return False   #방문한 경우

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
result =  0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)