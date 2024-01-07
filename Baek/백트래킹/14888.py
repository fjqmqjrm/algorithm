N = int(input())

an = list(map(int,input().split()))
op = list(map(int,input().split()))

m = 1e+10
M = -(1e+10)
def dfs(n,num):
    global m,M
    if n == N-1:
        if m > num:
            m = num
        if M < num:
            M = num
        return

    for i in range(4):
        if op[i] == 0:
            continue
        if i == 0:
            op[i] -= 1
            dfs(n+1,num+an[n+1])
            op[i] += 1
        if i == 1:
            op[i] -= 1
            dfs(n+1,num-an[n+1])
            op[i] += 1
        if i == 2:
            op[i] -= 1
            dfs(n+1,num*an[n+1])
            op[i] += 1
        if i == 3:
            op[i] -= 1
            if abs(num) != num:
                v = abs(num)//an[n+1]
                dfs(n+1,-v)
            else:
                dfs(n+1,num//an[n+1])
            op[i] += 1

dfs(0,an[0])

print(M)
print(m)
