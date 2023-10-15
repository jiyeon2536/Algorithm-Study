N = int(input())
box = [list(map(str, input())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    global visited, cnt
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        x, y = q.pop(0)
        color = box[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx in range(0, N) and ny in range(0, N) and visited[nx][ny] == 0 and box[nx][ny] == color:
                visited[nx][ny] = 1
                q.append((nx, ny))

# 적록색약 아닌 사람
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt1 += 1

# G -> R
for i in range(N):
    for j in range(N):
        if box[i][j] == 'G':
            box[i][j] = 'R'

# 적록색약인 사람
visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)
