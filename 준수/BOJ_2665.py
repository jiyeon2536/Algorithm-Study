from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
maze = [list(map(int, input())) for _ in range(N)]

ex, ey = N - 1, N - 1

cost_matrix = [[int(1e9)] * N for _ in range(N)]
cost_matrix[0][0] = 0

queue = deque()
queue.appendleft((0, 0))

while queue:
    x, y = queue.popleft()

    if x == ex and y == ey:
        print(cost_matrix[ex][ey])
        break

    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < N and 0 <= ny < N and cost_matrix[nx][ny] > cost_matrix[x][y]:
            if maze[nx][ny]:
                cost_matrix[nx][ny] = cost_matrix[x][y]
                queue.appendleft((nx, ny))
            else:
                cost_matrix[nx][ny] = cost_matrix[x][y] + 1
                queue.append((nx, ny))