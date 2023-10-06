def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    queue = deque([[0, 0, 0]])

    while queue:
        x, y, z = queue.popleft()

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < M:
                if plane[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    queue.append([nx, ny, z])
                    visited[nx][ny][z] = visited[x][y][z] + 1

                if plane[nx][ny] == 1 and visited[nx][ny][z] == 0 and z < 1:
                    queue.append([nx, ny, z + 1])
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1

    mn_cost = 10000000000000000

    for cost in visited[N - 1][M - 1]:
        if not cost == 0 and mn_cost > cost:
            mn_cost = cost

    if mn_cost == 10000000000000000:
        print(-1)
    else:
        print(mn_cost)


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
plane = [list(map(int, list(input()))) for _ in range(N)]
bfs()