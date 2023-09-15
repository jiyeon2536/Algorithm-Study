def bfs(lst):
    queue = deque()
    cnt = -1

    for t in lst:
        queue.append(t)

    while queue:
        cnt += 1
        for _ in range(len(queue)):
            vertex = queue.popleft()
            x = vertex[0]
            y = vertex[1]
            z = vertex[2]

            for move in range(6):
                nx = x + dx[move]
                ny = y + dy[move]
                nz = z + dz[move]

                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomato[nz][nx][ny] == 0:
                    queue.append([nx, ny, nz])
                    tomato[nz][nx][ny] = 1

    return cnt


from collections import deque

N, M, H = map(int, input().split())

start = []
tomato = []

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

for h in range(H):
    plane = []

    for m in range(M):
        line = list(map(int, input().split()))

        for idx in range(N):
            if line[idx] == 1:
                start.append([m, idx, h])

        plane.append(line)

    tomato.append(plane)

res = True
res_cnt = bfs(start)

for k in range(H):
    for i in range(M):
        for j in range(N):
            if tomato[k][i][j] == 0:
                res = False
                break

if res:
    print(res_cnt)
else:
    print(-1)
