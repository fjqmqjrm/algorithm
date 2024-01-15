# 11005 - 진법 변환2 (ok)
# 10진법 수 N을 B진법 수로 변환
N, B = map(int,input().split())
nst = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tot = ""
C = N
NA = B
count = 0
while(True):
    if C < B :
        tot += nst[C]
        break
    NA = C%B
    tot+= nst[NA]
    C = C//B

tot = list(tot)
tot.reverse()
totst = ""
for _ in tot:
    totst += _
print(totst)

