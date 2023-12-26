# 시각 설명
# 정수 N이 입력되면 00시00분00초 부터 N시 59분 59초 까지의 모든 시각 중 3이 하나라도 포함되는 경우의 수를 구하시오

n = int(input())

result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                result += 1

print(result)