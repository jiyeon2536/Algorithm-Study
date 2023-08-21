import sys
input = sys.stdin.readline
from collections import deque

def bfs(coord):
    queue = deque()
    queue.append(coord)

    # 인접한 음식물의 수
    cnt = 0

    while queue:
        x, y = queue.popleft()
        # 인접한 음식물이 있을 경우
        cnt += 1

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M and passage[nx][ny] == 1:
                # 중복 탐색을 허용하지 않음
                passage[nx][ny] = 0
                queue.append([nx, ny])

    return cnt

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().split())
# 깨끗한 복도
passage = [[0] * M for _ in range(N)]

# 복도 위에 음식물 표시
for _ in range(K):
    r, c = map(int, input().split())
    passage[r-1][c-1] = 1

mx = 0

for i in range(N):
    for j in range(M):
        # 음식물을 발견하면
        if passage[i][j] == 1:
            passage[i][j] = 0
            # 인접한 음식물이 있는지 탐색
            res = bfs([i, j])

            if res > mx:
                mx = res

print(mx)