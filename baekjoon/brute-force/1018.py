# 1018 - 체스판 다시 칠하기 (20240102) ok
N,M = map(int, input().split())
boardLi = []
bestLi1 = []
bestLi2 = []
# 해당 행렬 수로 나올 수 있는 최적 보드 2가지

for i in range(4):
    bestLi1.append("BWBWBWBW")
    bestLi1.append("WBWBWBWB")
for i in range(4):
    bestLi2.append("WBWBWBWB")
    bestLi2.append("BWBWBWBW")


for i in range(N):
    boardLi.append(input())

min = M*N
i = 0
j = 0

while True:
    li = []
    for k in range(i,i+8):
        str = ""
        for s in range(j,j+8):
            str = str + boardLi[k][s]
        li.append(str)
    count = 0
    for a in range(8):
        for b in range(8):
            if bestLi1[a][b] != li[a][b]:
                count += 1
    if min > count:
        min = count
    count = 0
    for a in range(0,8):
        for b in range(0,8):
            if bestLi2[a][b] != li[a][b]:
                count += 1
    if min > count:
        min = count
    if i+7 <= N-1:
        i += 1
    if i+7 > N-1:
        i = 0
        j += 1
    if j+7 > M-1:
        break
print(min)







