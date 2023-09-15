import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()

tomatoes = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x] == 1:
                queue.append([x, y, z])
            elif arr[z][y][x] == 0:
                tomatoes += 1

cnt = 0
day = 0
while queue:
    if tomatoes == 0:
        break
    elif cnt == 0:
        cnt = len(queue)
        day += 1
    x, y, z = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and not arr[nz][ny][nx]:
            arr[nz][ny][nx] = 1
            queue.append([nx, ny, nz])
            tomatoes -= 1
    cnt -= 1

if tomatoes > 0:
    print(-1)
else:
    print(day)