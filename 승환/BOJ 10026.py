def dfs1(x):
    global cnt1
    cnt1 += 1
    i = x[0]
    j = x[1]
    col = x[2]
    visited1[i][j] = 1
    q = [[i, j]]
    while q:
        t = q.pop(0)
        x, y = t[0], t[1]
        visited1[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited1[nx][ny] == 0 and arr[nx][ny] == col:
                visited1[nx][ny] = 1
                q.append([nx, ny])


def dfs2(x):
    global cnt2
    cnt2 += 1
    i = x[0]
    j = x[1]
    if x[2] == 'R' or x[2] == 'G':  # 적록 색약인 경우 색을 바꾸어 준다.
        col = ['R', 'G']
    else:
        col = ['B']
    visited2[i][j] = 1
    q = [[i, j]]
    while q:
        t = q.pop(0)
        x, y = t[0], t[1]
        visited2[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited2[nx][ny] == 0 and arr[nx][ny] in col:
                visited2[nx][ny] = 1
                q.append([nx, ny])


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt1 = 0
cnt2 = 0
n = int(input())
arr = [list(input()) for _ in range(n)]
visited1 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            col = arr[i][j]
            dfs1([i, j, col])
visited2 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            col = arr[i][j]
            dfs2([i, j, col])
print(cnt1, cnt2)
