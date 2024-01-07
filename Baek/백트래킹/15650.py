n, m = map(int,input().split())

visited = [False] * (n+1)
depth = 0
def dfs(depth,lst,element):
    if depth == m:
        print(*lst)
        return
    for i in range(1,n+1):
        if element > i:
            continue
        if not visited[i]:
            visited[i] =True
            dfs(depth+1, lst+[i],i)
            visited[i] = False
dfs(0,[],0)