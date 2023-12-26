# 문자열 재졍렬
# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순 순으로 정렬하여
# 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어 출력합니다
# 숫자는 0~9 사이 하나를 뜻함 수와 다른 뜻


st = input()
num = 0
slist = []
for s in st:
    if s.isdigit():
        num+=int(s)
    else:
        slist.append(s)
slist.sort()
if num != 0:
    slist.append(str(num))

#list 출력하는 방식
print(''.join(slist))