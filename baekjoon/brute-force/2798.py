# 2798 - 블랙잭 (20240105) ok
N, M = map(int,input().split())
cardNums = list(map(int,input().split()))
numTot = 0
totLi = []
#index :  0~n-1
def add(a,b,c):
    return a+b+c
n1,n2,n3 = 0,1,2

for i in range(n1,N):
    for j in range(n2,N):
        for k in range(n3,N):
            if i!=j and i!=k and j!=k and add(cardNums[i], cardNums[j], cardNums[k]) <= M:
                totLi.append(add(cardNums[i], cardNums[j], cardNums[k]))
totLi.sort()
print(totLi[-1])

