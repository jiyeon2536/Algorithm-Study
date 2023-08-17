def dfs(depth, arr, closed):
    new_closed = closed[:]

    if depth == M:
        return bfs(arr)

    for v in range(len(chicken)):
        if new_closed[v] == False:
            new_closed[v] = True
            dfs(depth + 1, arr + [chicken[v]], new_closed)


def bfs(arr):
    global mn

    visited = [[False] * N for _ in range(N)]
    queue = deque(arr)
    distance = 0

    new_city = []

    for n in city:
        tmp_line = []
        for m in n:
            if m == 2:
                tmp_line.append(0)
            else:
                tmp_line.append(m)
        new_city.append(tmp_line)

    while queue:
        distance += 1
        for _ in range(len(queue)):
            coord = queue.popleft()
            x = coord[0]
            y = coord[1]
            visited[x][y] = True

            for move in range(4):
                nx = x + dx[move]
                ny = y + dy[move]

                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                    if new_city[nx][ny] == 1:
                        new_city[nx][ny] = distance

    res = 0

    for r in range(N):
        for c in range(N):
            if new_city[r][c]:
                res += new_city[r][c]

    if mn > res:
        mn = res


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

city = []
chicken = deque()

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            chicken.append([i, j])
    city.append(line)

closed_chicken = [False] * len(chicken)

mn = 980309
dfs(0, [], closed_chicken)

print(mn)