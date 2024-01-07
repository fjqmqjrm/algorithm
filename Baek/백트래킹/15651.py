n, m = map(int,input().split())

depth = 0
def dfs(depth,lst):
    if depth == m:
        print(*lst)
        return
    for i in range(1,n+1):
        dfs(depth+1, lst+[i])

dfs(0,[])