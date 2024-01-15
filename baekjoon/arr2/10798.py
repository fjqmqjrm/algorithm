# 10798 - 세로읽기 (20240115) ok
li = [["" for j in range(15)]for i in range(5)]

for _ in range (5):
    str = input()
    for i in range (len(str)):
        li[_][i] = str[i]

reStr = []
fistr = ""
for _ in range(15):
    for i in range(5):
        if li[i][_] !=  "":
            reStr.append(li[i][_])
for _ in range(len(reStr)):
    fistr += reStr[_]
print(fistr)