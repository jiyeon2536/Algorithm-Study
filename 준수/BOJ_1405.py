def dfs(x, y, depth, result):
    global answer

    if result == 0:
        return

    if depth == N:
        answer += result
        return

    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        if (nx, ny) not in move_coord:
            move_coord.add((nx, ny))
            dfs(nx, ny, depth + 1, result * (chance[move] / 100))
            move_coord.remove((nx, ny))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, *chance = list(map(int, input().split()))
move_coord = set()
move_coord.add((0, 0))
answer = 0
dfs(0, 0, 0, 1)
print(answer)
