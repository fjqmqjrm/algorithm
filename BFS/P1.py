from collections import deque


def bfs(g,vertex , visited):
    queue = deque([vertex])
    visited[vertex] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in g[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

bfs(graph,1,visit)