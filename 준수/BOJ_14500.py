def dfs(num, x, y, sum):
    global visited
    global mx

    if num == 4:
        if mx < sum:
            mx = sum
        return
    
    if mx and mx < sum:
        return

    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            if num == 2:
                visited[nx][ny] = True
                dfs(num + 1, x, y, sum + paper[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(num + 1, nx, ny, sum + paper[nx][ny])
            visited[nx][ny] = False


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
mx = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, i, j, paper[i][j])
        visited[i][j] = False

print(mx)