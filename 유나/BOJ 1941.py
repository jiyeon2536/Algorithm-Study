import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

girls = [list(input().strip()) for _ in range(5)]
positions = [(i, j) for i in range(5) for j in range(5)]
# 25C7 25명의 학생 중 7명 뽑기
combs = list(combinations(positions,7))

# 도연이네가 3명 초과인지 체크
def ds_chk(comb):
    yy = 0
    for x, y in comb:
        if girls[x][y] == 'Y':
            yy += 1
            if yy > 3:
                return False
    return True

# 인접해있는지 체크
def ds_pass(comb):
    visited = [0] * 7
    que = deque()
    que.append(comb[0])
    visited[0] = 1

    while que:
        x, y = que.popleft()
        for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in comb:
                next = comb.index((nx, ny))
                if not visited[next]:
                    que.append((nx, ny))
                    visited[next] = 1
    if 0 in visited:
        return False
    return True



cnt = 0
for comb in combs:
    if ds_chk(comb):
        if ds_pass(comb):
            cnt += 1

print(cnt)
