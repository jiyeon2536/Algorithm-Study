def bfs(x, y):
    global visited, box
    queue = [(x, y)]
    visited[x][y] = True
    cnt = 0

    while queue:
        i, j = queue.pop(0)
        cnt += 1
        for di, dj in [0, 1], [1, 0], [-1, 0], [0, -1]:
            ni, nj = i + di, j + dj
            if ni in range(0, M) and nj in range(0, N) and box[ni][nj] == box[i][j] and visited[ni][nj] == False:
                queue.append([ni, nj])
                visited[ni][nj] = True
    return cnt

N, M = map(int, input().split())  # 가로N 세로M
box = [list(map(str, input())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
W = B = 0

for m in range(M):
    for n in range(N):
        if visited[m][n] == False:
            p = bfs(m,n)
            if box[m][n] == 'W':
                W += p ** 2
            else:
                B += p ** 2

print(W, B)
