def boj2206():
    import sys
    input = sys.stdin.readline
    from collections import deque 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N, M = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[[-1] * M for _ in range(N)] for _ in range(2)]
    z = 0

    def bfs():
        nonlocal visited
        nonlocal z
        q = deque()
        q.append((0, 0, 0))
        visited[0][0][0] = 1
        while q:
            z, x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    # 벽을 부수지 않았고, 현실세계의 벽이 아닐때
                    if arr[nx][ny] == 0 and visited[z][nx][ny] == -1:
                        visited[z][nx][ny] = visited[z][x][y] + 1
                        q.append((z, nx, ny))
                    # 벽인 경우 벽을 부수지 않았을 때,
                    if arr[nx][ny] == 1 and visited[z][nx][ny] == -1:
                        if z == 0:
                            visited[1][nx][ny] = visited[z][x][y] + 1
                            q.append((1, nx, ny))
                        # 벽을 부쉈을 때
                        elif z == 1:
                            continue
    bfs()
    print(visited[z][N-1][M-1])


boj2206()
