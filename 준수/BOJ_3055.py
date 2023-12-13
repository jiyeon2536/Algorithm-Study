def bfs(queue):
    time = 0

    while queue:
        time += 1

        for _ in range(len(queue)):
            x, y, z = queue.popleft()

            for move in range(4):
                nx = x + dx[move]
                ny = y + dy[move]

                if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] not in ('X', '*'):
                    if z:
                        if forest[nx][ny] == '.':
                            forest[nx][ny] = '-'
                            queue.append((nx, ny, 1))
                        elif forest[nx][ny] == 'D':
                            print(time)
                            return
                    else:
                        if forest[nx][ny] in ('.', '-'):
                            forest[nx][ny] = '*'
                            queue.append((nx, ny, 0))

    print('KAKTUS')
    return


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]

si, sj = -1, -1

arr = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            si, sj = i, j
            forest[i][j] = '-'

        if forest[i][j] == 'D':
            ei, ej = i, j

        if forest[i][j] == '*':
            arr.append((i, j, 0))

arr.append((si, sj, 1))

bfs(arr)
