# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익게 된다.
# 6방향에 영향을 준다.
# H는 층 수 이다.
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸
from collections import deque
import sys
from collections import deque
input = sys.stdin.readline
tomato = deque()


def f(tomato):
    dx = [-1, 0, 0, 1, 0, 0]  
    dy = [0, 1, -1, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]  # 위층 고려
    while tomato:
        z, x, y =tomato.popleft()
        visited[z][x][y] = 1
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and arr[nz][nx][ny] == 0:
                # 이 지점에서 사방탐색(높이까지 고려해서 6방향)해서 최솟값을 줘야한다.
                visited[nz][nx][ny] = 1
                arr[nz][nx][ny] = arr[z][x][y] + 1
                tomato.append((nz, nx, ny))


M, N, H = list(map(int, input().split()))
height = N * H
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                tomato.append((h, i, j))
f(tomato)
mx = 0
for z in range(H):
    if mx == -1:
        break
    for i in range(N):
        if mx == -1:
            break
        for j in range(M):
            if arr[z][i][j] == 0:
                mx = -1
                break
            if arr[z][i][j] - 1 > mx:
                mx = arr[z][i][j] - 1
print(mx)
