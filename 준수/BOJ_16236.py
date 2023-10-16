def find_fish(fx, fy):
    visited = [[False] * N for _ in range(N)]
    queue = [[fx, fy]]
    time = 0

    while queue:
        tmp = []
        for _ in range(len(queue)):
            x, y = queue.pop(0)

            if space[x][y] > 0 and space[x][y] < baby_shark_size:
                tmp.append([x, y])

            for move in range(4):
                nx = x + dx[move]
                ny = y + dy[move]

                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and space[nx][ny] <= baby_shark_size:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

        if tmp:
            tmp.sort(key=lambda coord: coord[1])
            tmp.sort(key=lambda coord: coord[0])
            return tmp[0][0], tmp[0][1], time

        time += 1

    return -1, -1, -1


def bfs(sx, sy):
    global baby_shark_size
    global baby_shark_eat

    queue = [[sx, sy]]
    total_time = 0

    while queue:
        x, y = queue.pop(0)
        
        nx, ny, time = find_fish(x, y)

        if nx == ny == time == -1:
            print(total_time)
            return

        total_time += time

        queue.append([nx, ny])

        baby_shark_eat += 1

        if baby_shark_eat == baby_shark_size:
            baby_shark_eat = 0
            baby_shark_size += 1

        space[nx][ny] = 0

    print(total_time)


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

space = []

baby_shark_x = 0
baby_shark_y = 0

baby_shark_size = 2
baby_shark_eat = 0

N = int(input())

for i in range(N):
    line = list(map(int, input().split()))

    for j in range(N):
        if line[j] == 9:
            baby_shark_x = i
            baby_shark_y = j
            line[j] = 0

    space.append(line)

bfs(baby_shark_x, baby_shark_y)