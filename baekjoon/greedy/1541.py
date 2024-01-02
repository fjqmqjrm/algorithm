# 1541 - 잃어버린 괄호 (20240101) ok
from collections import deque

inputValue = input()
li = []
calLi = deque()
for i in inputValue:
    li.append(i)
check = ""
for j in range (len(li)):
    if li[j] == '-':
        if check != "":
            calLi.append(str(eval(check)))
            check = ""
        calLi.append(li[j])
    else:
        check += li[j]
        if check == "0" :
            check = ""
        if "+0" in check :
            check = check[:-1]

    if j == len(li)-1:
        calLi.append(str(eval(check)))
        #print(calLi)
finalCal = ""
for i in calLi:
    finalCal += i
print(eval(finalCal))




