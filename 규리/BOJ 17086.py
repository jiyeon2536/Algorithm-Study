N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

q = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
            box[i][j] = 0
        else:
            box[i][j] = -1

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

while q:
    x, y = q.pop(0)
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if nx in range(0, N) and ny in range(0, M) and box[nx][ny] == -1:
            box[nx][ny] = box[x][y] + 1
            q.append((nx, ny))
mx = 0
for i in box:
    mx = max(max(i), mx)
print(mx)
