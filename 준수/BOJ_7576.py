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

            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]

                if 0 <= nx < M and 0 <= ny < N and tomato[nx][ny] == 0:
                    queue.append([nx, ny])
                    tomato[nx][ny] = 1

    return cnt


from collections import deque

N, M = map(int, input().split())
start = []
tomato = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for m in range(M):
    tmp_arr = list(map(int, input().split()))

    for idx in range(N):
        if tmp_arr[idx] == 1:
            start.append([m, idx])

    tomato.append(tmp_arr)

res = True
res_cnt = bfs(start)

for i in range(M):
    for j in range(N):
        if tomato[i][j] == 0:
            res = False
            break

if res:
    print(res_cnt)
else:
    print(-1)
