'''
0 - (재귀 호출)
유클리드 호제법
두 자연수의 A, B에 대하여(A>B) A%B = R이라 할 때,
A와B의 최대공약수는 B와R의 최대공약수와 같다.'''
def gcd(a, b):
    if a % b == 0 : # a가 b의 배수라면 (나머지가 없다면)
        return b
    else :
        return gcd(b, a % b)

print(gcd(192,162))