# 음료수 얼려먹기 문제
# N x M 크기의 얼음 틀이 있습니다. 구멍이 뚤려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚤려있는 부분끼리 상하좌우로 붙어있는 경우 연결되어 있는 것으로 간주됩니다.
# 이때 생산되는 아이스크림의 총 개수를 구하는 프로그램을 작성하시오

graph = []
def dfs(x,y):
    if x<=-1 or x >=n or y <=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] =1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
n,m = map(int,input().split())


for i in range(n):
    graph.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)