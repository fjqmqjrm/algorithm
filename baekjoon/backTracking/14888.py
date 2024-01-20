# 14888 - 연산자 끼워넣기 (ok)
import sys
from copy import copy
input = sys.stdin.readline

# 입력
N = input()
numAry = list(map(int,input().split())) # 쪼갠 뒤, 리스트 저장
countOper = list(map(int,input().split())) # 연산자 수
operLi = []
# 사용 가능한 연산자 담아두기
for i in range(countOper[0]):
    operLi.append("+")
for i in range(countOper[1]):
    operLi.append("-")
for i in range(countOper[2]):
    operLi.append("*")
for i in range(countOper[3]):
    operLi.append("/")
# 연산자 방문 여부
operCheck = [False] * len(operLi)
ans = []
fi_Li = []
def b_t (operCheck,ans):
    if len(ans) == len(operLi):
        this_ans = copy(ans)
        fi_Li.append(this_ans)
        return
    else:
        for i in range (len(operLi)):
            if operCheck[i] == False:
                operCheck[i] = True
                ans.append(operLi[i])
                b_t(operCheck,ans)
                ans.pop()
                operCheck[i] = False
def cal(num1,oper,num2):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2
    if oper == '/':
        if num1 < 0 and num2 > 0 :
            num1 = -num1
            return  -(num1//num2)
        else:
            return num1 // num2
b_t(operCheck,ans)
totLi = []
for oper in fi_Li:
    tot = 0
    for i in range(len(numAry)):
        if i == 0:
            tot += numAry[0]
        else:
            tot = cal(tot,oper[i-1],numAry[i])
    totLi.append(tot)

print(max(totLi))
print(min(totLi))



