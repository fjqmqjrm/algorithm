# 깊이 탐색 예제

def dfs(g,vertex,visited):
    visited[vertex] = True
    print(vertex , end=' ')
    for i in g[vertex]:
        if not visited[i]:
            dfs(g,i,visited)



visit = [False]*9

graph = [
    [1,3,5],
    [0,2,3,6],
    [0,1,5,6],
    [2,4,5],
    [0,1,6],
    [],
    [2,4,5]
]
dfs(graph,0,visit)
