# N과 K가 주어졌을 때 N을 K로 나누거나 N에 1을 빼는 동작을 수행 할 수 있다
# 최소한의 연산 횟수로 N을 1로 만들어라
# p1
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어지지 않는 상황에서 가장 가까운 나누어지는 값을 찾는 방법
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)

print(result)