# 최대 공약수 구하기 문제
# 유클리드 호재법을 이용하여 해결 가능
# 유클리드 호재법 : A와 B의 최대 공약수는 B와 A를 B로 나눈 나머지의 최대 공약수와 같다 (A>B)
a,b = map(int, input().split())

if a<b:
    raise RuntimeError

def gcd(j,k):
    if j%k == 0:
        return k

    return gcd(k,j%k)

result = GCD(a,b)
print(result)

