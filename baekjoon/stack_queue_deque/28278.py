# 28278 - 스택2 (ok)
import sys
input = sys.stdin.readline
stack = []
N = int(input())
prinLi = []
for i in range(N):
    orderNum = input()
    if '1' in orderNum :
        a,b = orderNum.split()
        stack.append(int(b))
    elif '2' in orderNum:
        if len(stack) == 0:
            prinLi.append(-1)
        else:
            prinLi.append(stack.pop())

    elif '3' in orderNum:
        prinLi.append(len(stack))
    elif '4' in orderNum:
        if len(stack) == 0:
            prinLi.append((1))
        else :
            prinLi.append(0)
    else:
        if len(stack) != 0 :
            prinLi.append(stack[-1])
        else:
            prinLi.append(-1)
for i in prinLi:
    print(i)