n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))


count = []

def dfs(x,y):
    if x >= n or x < 0 or y>=n or y<0:
        return 0
    if graph[x][y] != 0:
        graph[x][y] = 0
        val = 1
        val += dfs(x-1,y)
        val += dfs(x,y-1)
        val += dfs(x+1,y)
        val += dfs(x,y+1)
        return val
    if graph[x][y] == 0:
        return 0

for i in range(n):
    for j in range(n):
        val = dfs(i,j)
        if val != 0:
            count.append(val)
print(len(count))
count.sort()
for s in count:
    print(s)