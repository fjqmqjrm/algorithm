n = int(input())
m = int(input())

def dfs(v):
    if not mask[v]:
        mask[v] = True
        for i in range(1,m+1):
            if v==graph[i][0]:
                dfs(graph[i][1])
            if v==graph[i][1]:
                dfs(graph[i][0])


graph = [[0,0]]
mask = [False]*(n+1)

for i in range(m):
    graph.append(list(map(int,input().split())))
graph.sort(key=lambda x: x[1])


dfs(1)

print(mask.count(True)-1)
