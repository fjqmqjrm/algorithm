# 11047 - 동전 0 (20240101)
n,k = input().split()
n,k = int(n) , int(k)
num ,count = 0,0 # 누적합계 계산, 동전 개수
weightli = []
for i in range(n): # 오름차순 리스트
    weightli.append(int(input()))

for i in range(n-1,-1,-1): # 동전 사용가능 인덱스 최댓값
    if weightli[i] <= k:
        indexPoint = i
        break
while (num != k):
    num += weightli[indexPoint]
    count += 1
    if num > k :
        num -= weightli[indexPoint]
        count -= 1
        indexPoint -= 1
print(count)




