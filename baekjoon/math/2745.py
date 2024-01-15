# 2745 - 진법 변환 (답안 참고)
N, B = input().split()
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0

for x in range(len(N)):
    sum = number.index(N[x]) * (B**x)
    result += sum

print(result)
