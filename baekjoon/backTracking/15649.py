# 15649 - N과 M
# 1부터 N까지 중복 없이 M개를 고른 수열 (사전순 증가 출력)

N, M = map(int,input().split())
NumLi = []
for i in range(1,N+1): # 1~N까지 담겨있는 리스트
    NumLi.append(i)
checkLi = [False]*N
ans = []
def re(cli,ans):
    if len(ans) == M:
        print(*ans)
        return
    else :
        for i in range(N):
            if cli[i] == False:
                cli[i] = True
                ans.append(NumLi[i])
                re(cli,ans)
                cli[i] = False
                ans.pop(-1)


re(checkLi,ans)

