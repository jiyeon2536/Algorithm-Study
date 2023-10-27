import math
import pprint
# 한캐릭터 최대 15분 최대 m 개 캐릭만
# 캐릭터마다 각 보스는 1회만

n, m, k = map(int, input().split())

character = []
for _ in range(n):
    character.append(int(input()))
boss = [[0,0]]
for j in range(k):
    w, v = map(int, input().split())
    ch = [v]
    for i in range(n): # w 보스 체력 ch 데미지 dps
        if w % character[i] > 0:
            a = int(w / character[i])+1
        else:
            a = int(w / character[i])
        ch.append(a)
    boss.append(ch)

rs = []

for x in range(1, n+1):
    mat = [[0] * (901) for _ in range(k + 1)]
    for i in range(1, k+1):
        for j in range(1, 901):
            if j < boss[i][x]:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(mat[i-1][j], boss[i][0]+mat[i-1][j-boss[i][x]])
    rs.append(mat[k][900])

cnt = 0
rs.sort(reverse=True)
for i in range(m):
    cnt += rs[i] #

print(cnt)




