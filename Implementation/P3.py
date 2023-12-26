# 왕실의 나이트
# 행복 왕국의 왕실 정원은 체스판과 같은 8x8 좌표평면입니다. 왕실 정원의 특정한 한 칸에 나이트가 서 있습니다
# 나이트는 말을 타고 있기에 이동 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로 나갈 수 없습니다.
# 나이트는 특정위치에서 2가지 경로로 이동 가능합니다.
# 1. 수평으로 두칸 이동 후 수직으로 한칸 이동 2. 수직으로 두 칸 이동 후 수평으로 한칸 이동
# 나이트의 위치가 주어졌을 때 나이트가 이동 할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요

pos = input()
xposList = ['a','b','c','d','e','f','g','h']
yposList = ['1','2','3','4','5','6','7','8']
xmov= [1,-1,2,-2]
ymove=[2,-2,1,-1]
result = 0
# ord 함수는 아스키코드 변환 함수
x = int(pos[1])
y = int(ord(pos[0]))-int(ord('a'))+1
for i in range(4):
    for j in range(4):
        dx = xmov[i]+x
        dy = ymove[j]+y
        if dx<1 or dy<1 or dx>8 or dy>8:
            continue
        result += 1
result //=2
print(result)