land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]

N = len(land[0])
M = len(land)

def dfs1(x,y):
    if x>=N or x<0 or y>=M or y<0 or [x,y] in mask:
        return 0

    if land[y][x] == 0:
        return 0
    if land[y][x] == 1 and [x,y] not in mask:
        mask.append([x,y])
        val = land[y][x]
        val+= dfs1(x-1,y)
        val+= dfs1(x+1,y)
        val+=dfs1(x,y-1)
        val+= dfs1(x,y+1)
        return val
    else:
        mask.append([x,y])
        return land[y][x]

def put_data(val):
    for s in mask:
        land[s[1]][s[0]] = val


mask = []
old_mask = []
data = []


for i in range(N):
    curData = []
    count = 0
    for j in range(M):
        value = dfs1(i,j)
        if value == 0:
            count =0
        if value != 0:

            put_data(value)
            if count == 0:
                curData.append(value)
            count +=1
    mask.clear()
    data.append(curData)

result =[]
for items in data:
    r = sum(items)
    result.append(r)
print(max(result))
