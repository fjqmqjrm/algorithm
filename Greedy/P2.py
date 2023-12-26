#곱하기와 더하기를 입력받은 숫자 사이에 넣어 가장 큰 숫자를 만드시오
#사칙연산의 우선순위는 무시하고 무조건 왼쪽에서부터 계산합니다.
#p2
n = input()

num = 0

for i in n:
    if num * int(i) > num:
        num *= int(i)
    else:
        num += int(i)

print(num)