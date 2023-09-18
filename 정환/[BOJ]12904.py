import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

possible = True


# 이지 피지 레몬스퀴지 ㅋㅋ
while S != T:
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
    if T == []:
        possible = False
        break

if possible:
    print(1)
else:
    print(0)