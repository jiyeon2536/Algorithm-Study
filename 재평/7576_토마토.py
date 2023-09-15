import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

tomatoes = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            queue.append([x, y])
        elif arr[y][x] == 0:
            tomatoes += 1

cnt = 0
day = 0
while queue:
    if tomatoes == 0:
        break
    elif cnt == 0:
        cnt = len(queue)
        day += 1
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not arr[ny][nx]:
            arr[ny][nx] = 1
            queue.append([nx, ny])
            tomatoes -= 1
    cnt -= 1

if tomatoes > 0:
    print(-1)
else:
    print(day)