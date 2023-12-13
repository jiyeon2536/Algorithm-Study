def bfs(sx, sy, sz):
    queue = [[sx, sy, sz]]
    snake_body = [[sx, sy]]
    time = 0

    while queue:
        x, y, z = queue.pop(0)
        
        time += 1
        nz = (z + dz[time]) % 4

        nx = x + dx[z]
        ny = y + dy[z]

        if 0 < nx < N + 1 and 0 < ny < N + 1 and [nx, ny] not in snake_body:
            snake_body.append([nx, ny])
            queue.append([nx, ny, nz])

            if board[nx][ny] == False:
                snake_body.pop(0)
            else:
                board[nx][ny] = False

    print(time)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [4] * 10001

N = int(input())
board = [[False for _ in range(N + 1)] for _ in range(N + 1)]

K = int(input())

for _ in range(K):
    r, c = map(int, input().split())

    board[r][c] = True

L = int(input())

for _ in range(L):
    time, rotate = input().split()

    if rotate == 'L':
        dz[int(time)] = 3
    else:
        dz[int(time)] = 5

bfs(1, 1, 1)