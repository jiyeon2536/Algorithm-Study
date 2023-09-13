# 토마토 2차원
import sys
from collections import deque
input = sys.stdin.readline
tomato = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(tomato):
    while tomato:
        x, y = tomato.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M  and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                tomato.append((nx, ny))


M, N = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i, j))
bfs(tomato)
mx = 0
for i in range(N):
    if mx == -1:
        break
    for j in range(M):
        if arr[i][j] == 0:
            mx = -1
            break
        if mx < arr[i][j] - 1:
            mx = arr[i][j] - 1
print(mx)
