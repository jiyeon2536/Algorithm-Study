import sys
input = sys.stdin.readline
from collections import deque

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
cashmap = [list(input().strip()) for _ in range(n)]

# 동전의 위치 파악
cashes = []
for i in range(n):
    for j in range(m):
        if cashmap[i][j] =='o':
            cashes.append((i, j))

# 기본 값 -1 지정
ans = -1
# cahses = [(동전1좌표), (동전2좌표), cnt]
def bfs(cashes):
    global ans
    que = deque()
    que.append(cashes)
    # 각 동전에 대한 visited!
    condition = False
    while que:
        # 첫 번재 동전과 두 번째 동전, 버튼 누른 횟수
        f, s, cnt = que.popleft()
        fx, fy = f
        sx, sy = s

        # 버튼 누를 힛수가 10이라면.. 앞으로 10 보다 커질 상황만 남았으니 break
        if cnt >= 10:
            break

        for dx, dy in [[0, 1], [0, -1], [1, 0],[-1, 0]]:
            nfx, nfy, nsx, nsy = fx+dx, fy+dy, sx + dx, sy +dy

            # 동전이 둘 다 벗어나지 않는다면
            if 0 <= nfx < n and 0 <= nfy < m and 0 <= nsx < n and 0 <= nsy < m:
                # 둘 다 벽이란 만난다면 pass
                if cashmap[nfx][nfy] == '#' and cashmap[nsx][nsy] == '#':
                    pass
                # 첫 번재 동전만 벽이라면, cnt + 1
                elif cashmap[nfx][nfy] == '#':
                    nxt_cnt = cnt + 1
                    que.append([(fx, fy), (nsx, nsy), nxt_cnt])
                # 두 번재 동전만 벽이라면, cnt + 1
                elif cashmap[nsx][nsy] == '#':
                    nxt_cnt = cnt + 1
                    que.append([(nfx, nfy), (sx, sy), nxt_cnt])
                # 둘 다 벽이 아니라면, cnt + 1
                else:
                    nxt_cnt = cnt + 1
                    que.append([(nfx, nfy), (nsx, nsy), nxt_cnt])
            # 둘 다 벗어난다면
            elif (nfx < 0 or nfx >= n or nfy < 0 or nfy >= m) and (nsx < 0 or nsx >= n or nsy < 0 or nsy >= m):
                pass
            # 하나만 벗어난다면
            else:
                ans = cnt + 1
                condition = True
                break
        if condition:
            break

bfs(cashes + [0])

print(ans)
