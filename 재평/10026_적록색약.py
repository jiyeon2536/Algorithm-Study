import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(x, y):
    visited[y][x] = 1
    color = arr[y][x]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == color and not visited[ny][nx]:
            DFS(nx, ny)

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

cnt = 0
dys_cnt = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            cnt += 1
            DFS(x, y)

visited = [[0]*N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if arr[y][x] == 'G':
            arr[y][x] = 'R'

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dys_cnt += 1
            DFS(x, y)

print(cnt, dys_cnt)