import pprint
# 메인 로직
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def sor(cnt, depth, start_i, start_j):
    global total
    if depth == num:
        total += cnt
        return

    for k in range(4):
        ni = start_i + di[k]
        nj = start_j + dj[k]

        if directions[k] == 0:
            continue

        newcnt = cnt * (directions[k] / 100 )


        if vis[ni][nj] == False:
            vis[start_i][start_j] = True
            sor(newcnt, depth+1, ni, nj)
            vis[start_i][start_j] = False

# 인풋
num , e, w, n, s = map(int, input().split())
directions = [e, w, s, n]
vis = [[False] * 28 for _ in range(28)]

total = 0
cnt = 1.0

# 아웃풋

sor(cnt, 0, 13, 13)
print(total)
