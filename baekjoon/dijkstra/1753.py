# 1753 - 최단경로 (ok)
INF = int(1e9)
# 입력
V, E = map(int,input().split()) # 정점 수 , 간선 수
start = int(input()) # 시작 노드

graph = [[]for i in range(V+1)]
# 간선 입력
for i in range(E):
    a, b ,c = map(int,input().split())
    graph[a].append((b,c))
# 최적 경로
distance = [INF] * (V+1) # 거리 초기화
visited = [False] * (V+1) # 방문 여부 초기화
def min(): # 방문하지 않은 노드들 중 가장 간선의 길이가 짧은 곳 찾기
    min_di = INF
    k = 0
    for i in range(1,V+1):
        if distance[i] < min_di and visited[i] == False:
            min_di = distance[i]
            k = i
    if k != 0:
        visited[k] = True
    return k

# 다익스트라
def dijkstra(start):
    distance[start] = 0 # 시작 노드에 대해선 거리 0으로 초기화
    visited[start] = True  # 시작 노드 방문 여부 수정
    for _ in graph[start]: # 시작 노드와 연결된 노드까지의 거리 초기화
        if distance[_[0]] == None :
            distance[_[0]] = _[1]
        elif distance[_[0]] > _[1]:
            distance[_[0]] = _[1]
        else :
            pass
    for i in range(V+1):
        min_node = min()
        if min_node != 0:
            for gr in graph[min_node]:
                if distance[gr[0]] > distance[min_node] + gr[1]:
                    distance[gr[0]] = distance[min_node] + gr[1]
        else:
            pass

dijkstra(start)
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

