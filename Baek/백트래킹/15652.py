n, m = map(int,input().split())


depth = 0
def dfs(depth,lst,element):
    if depth == m:
        print(*lst)
        return
    for i in range(1,n+1):
        if element > i:
            continue
        dfs(depth+1, lst+[i],i)
dfs(0,[],0)