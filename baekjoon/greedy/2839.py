# 2839 - 설탕 배달
N = int(input())
if N % 5 == 0 :
    print(N//5)
else :
    count = 0
    while True:
        N -= 3
        count += 1
        if N % 5 == 0 :
            count += N // 5
            print(count)
            break
        elif N < 0 :
            print(-1)
            break
        elif N == 0 :
            print(count)
            break


