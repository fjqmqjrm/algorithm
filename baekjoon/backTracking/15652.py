# 15652 - N과 M(4) (ok)
import sys
from copy import copy
input = sys.stdin.readline
N, M = map(int,input().split())
# 같은것이 있는 순열 - 오름차순
ans = []
fi_li = []
def back_t(ans):
    if len(ans) > 1 and ans[len(ans)-1] < ans[len(ans)-2]:
        return
    elif len(ans) == M:
        this_ans = copy(ans)
        fi_li.append(this_ans)
        return
    else:
        for i in range(1,N+1):
            ans.append(i)
            back_t(ans)
            ans.pop()
back_t(ans)
for i in fi_li:
    print(*i)

