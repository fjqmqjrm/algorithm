from collections import deque

n,m,v = map(int,input().split())

graph = [[0,0]]
for i in range(m):
    graph.append(list(map(int,input().split())))
graph.sort(key=lambda x:x[1])
visit = [False]*(n+1)

visit2 = [False]*(n+1)
def dfs(v,visited):
    if not visited[v]:
        print(v,end=" ")
        visited[v] = True
        for i in range(1,m+1):
            if graph[i][0] == v and not visited[graph[i][1]]:
                dfs(graph[i][1],visited)
            if graph[i][1] == v and not visited[graph[i][0]]:
                dfs(graph[i][0],visited)
        return


def bfs(v,visited2):
    q = deque([v])

    while q:
        v=q.popleft()
        visited2[v] = True
        print(v,end=" ")
        for i in range(1,m+1):
            if graph[i][0] == v:
                if not visited2[graph[i][1]]:
                    visited2[graph[i][1]] = True
                    q.append(graph[i][1])

            if graph[i][1]==v:
                if not visited2[graph[i][0]]:
                    visited2[graph[i][0]] = True
                    q.append(graph[i][0])


dfs(v,visit)
print(end="\n")
bfs(v,visit2)