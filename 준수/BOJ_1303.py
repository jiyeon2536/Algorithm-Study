def bfs(sx, sy, color):
    global w_sum
    global b_sum

    queue = [[sx, sy]]
    bag[sx][sy] = 'N'
    cnt = 1

    while queue:
        x, y = queue.pop(0)

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < M and 0 <= ny < N and bag[nx][ny] == color:
                bag[nx][ny] = 'N'
                queue.append([nx, ny])
                cnt += 1

    if color == 'W':
        w_sum += cnt ** 2
    else:
        b_sum += cnt ** 2


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
bag = [list(input()) for _ in range(M)]

w_sum = 0
b_sum = 0

for i in range(M):
    for j in range(N):
        if bag[i][j] in ['W', 'B']:
            bfs(i, j, bag[i][j])

print(w_sum, b_sum)