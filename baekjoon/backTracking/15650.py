# 15650 - N과 M (2) (ok)
import sys
# 1~N 까지 자연수 중 중복 없이 M개 오름차순
from copy import copy # 외우기 - 리스트 같은 주소 이슈 해결 


def back_t(check,ans,l): # 방문여부, 출력 누적
    this_ans = copy(ans) # 같은 주소 참조하므로 값 따로 저장
    if len(this_ans) == M:
        fi_li.append(this_ans)
        return
    else:
        for j in range(l+1,N+1):
            if N+1-j < M-len(ans): #남.인덱스 < 남은 수
                return
            elif check[j] == False:
                    check[j] = True
                    ans.append(j)
                    back_t(check,ans,j)
                    ans.pop()
                    check[j] = False


N, M = map(int,sys.stdin.readline().split())
fi_li = [] # 최종 결과 순회할 리스트
check = [False]*(N+1)

for i in range(1,N+1):
    ans = []
    check[i] = True
    ans.append(i)
    if M == 1:
        fi_li.append(ans)
    else:
        back_t(check,ans,i)


for i in fi_li:
    print(*i)
