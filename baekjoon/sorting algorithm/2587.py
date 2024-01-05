# 2587 - 대표값2 (20240105) ok
numLi = []
for i in range(5):
    numLi.append(int(input()))
numLi.sort()
print(int((numLi[0]+numLi[1]+numLi[2]+numLi[3]+numLi[4])/5))
print(int(numLi[2]))