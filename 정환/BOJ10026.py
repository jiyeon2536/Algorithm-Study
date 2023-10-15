import sys
input = sys.stdin.readline


N = int(input())

# 적록색약이 아닌 분들을 위한 BFS
def bfs1(s, color):
    global cnt_red
    global cnt_green
    global cnt_blue
    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.pop(0)

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1

    if color == 'R':
        cnt_red += 1
    elif color == 'G':
        cnt_green += 1
    else:
        cnt_blue += 1

# 적록색약인 분들을 위한 BFS
def bfs2(s):
    global cnt_abnormal

    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

    while queue:
        n = queue.pop(0)

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] == 'R' or arr[ni][nj] == 'G':
                    queue.append([ni, nj])
                    visited[ni][nj] = 1

    cnt_abnormal += 1


arr = [input().strip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt_abnormal = 0

cnt_red = 0
cnt_green = 0
cnt_blue = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if arr[i][j] == 'R':
                bfs1([i, j], 'R')
            elif arr[i][j] == 'G':
                bfs1([i, j], 'G')
            elif arr[i][j] == 'B':
                bfs1([i, j], 'B')

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                bfs2([i, j])


print((cnt_red + cnt_green + cnt_blue), (cnt_abnormal + cnt_blue))
