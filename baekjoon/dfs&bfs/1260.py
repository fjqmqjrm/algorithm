from collections import deque
# 1260 - dfs/bfs (ok)
N, M ,V = map(int,input().split())
graph = [[]for k in range(N+1)]
kli = []
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    kli.append(a)
    kli.append(b)
for j in graph:
    j.sort()
# dfs
visited = [False] * (N+1)
def dfs(k):
    visited[k] = True
    print(k, end=" ")
    for x in graph[k]:
        if visited[x] == False :
            dfs(x)
dfs(V)

visited_2 = [False] * (N+1)
li = deque()
print()
li.append(V)
visited_2[V] = True
for k in graph[V]:
    if visited_2[k] == False:
        visited_2[k] = True
        li.append(k)
while True:
    for m in list(li):
        for o in graph[m]:
            if visited_2[o] == False:
                li.append(o)
                visited_2[o] = True
        if len(li) == 0:
            pass
        else:
            print(li.popleft(), end=" ")
    if len(li) == 0:
        break



