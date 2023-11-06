def bfs(arr):
    global answer
    sx, sy = arr[0]

    queue = list()
    queue.append((sx, sy))
    visited = [[True] * 5 for _ in range(5)]

    for x, y in arr[1:]:
        visited[x][y] = False

    cnt = 0

    while queue:
        x, y = queue.pop(0)
        cnt += 1

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))

    if cnt >= 7:
        answer += 1


def comb(select_arr, visited, count):
    if len(select_arr) == 7:
        if count >= 4:
            bfs(select_arr)
        return

    new_visited = []

    for temp in visited:
        new_visited.append(temp[:])

    for i in range(5):
        for j in range(5):
            if new_visited[i][j] == False:
                new_visited[i][j] = True
                if matrix[i][j] == "Y":
                    comb(select_arr + [(i, j)], new_visited, count)
                else:
                    comb(select_arr + [(i, j)], new_visited, count + 1)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

matrix = [list(input()) for _ in range(5)]
selected = [[False] * 5 for _ in range(5)]
answer = 0
comb([], selected, 0)
print(answer)
