# 24479 - 알고리즘 수업 - 깊이 우선 탐색1 (ok)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
dic = {} # 방문 순서 체크 딕셔너리
N, M, R = map(int,input().split())
graph = [[]for i in range(N+1)]
for i in range(M):
    u, v = map(int,input().split())
    # 각 노드의 연결 정보 추가
    graph[u].append(v)
    graph[v].append(u)
for j in range (len(graph)):
    graph[j] = sorted(graph[j])
visited = [False]*(N+1)
count = 1
def dfs(graph,R):
    global  count
    for i in graph[R]:
        if visited[i] == False:
            count+=1
            visited[i] = True
            dic[i] = count
            dfs(graph,i)
visited[R] = True
dic[R] = count
dfs(graph,R)
li = [0]*(N+1)
for i in range (1,N+1):
    try:
        li[i] = dic[i]
    except KeyError:
        pass
for i in range(1,N+1):
    print(li[i])