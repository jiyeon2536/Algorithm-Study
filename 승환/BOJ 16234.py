def baek16234():
    def bfs(a, b):
        nonlocal cnt
        nonlocal bp
        q = [[a, b]]
        chk = [[a, b]]
        sv = arr[a][b]
        while q:
            E = q.pop(0)
            x = E[0]
            y = E[1]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny <N and L <= abs(arr[x][y] - arr[nx][ny]) <= R and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if [nx, ny] in chk:
                        continue
                    chk.append([nx, ny])
                    q.append([nx, ny])
                    sv += arr[nx][ny]
        if len(chk) > 1:
            now = sv // len(chk)
            bp = 1
            # visited에 바꿔야 할 값을 넣어 놓는다.
            # 끝까지 돈다면 visited 값을 바꾸면서 배열 값 또한 바꾼다.?
            for m in range(len(chk)):
                nnx = chk[m][0]
                nny = chk[m][1]
                visited[nnx][nny] = now

    N, L, R = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 국경 선을 공유 하는 두 나라의 인구 차이가 L명 이상, R명 이하 라면,
    # 국경 선이 열려 있어 인접한 칸을 이용해 이동할 수 있으면, 연합
    # BFS 돌면서 인접한 나라 들을 확인 하고 한 번에 바꿔야 한다.
    # 연합을 이루고 있는 각 칸의 인구 수는 (연합의 인구수)/(연합을 이루고 있는 칸의 개수)
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while True:
        bp = 0
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    bfs(i, j)
        if bp == 0:
            break
        for i in range(N):
            for j in range(N):
                if visited[i][j] != 0:
                    arr[i][j] = visited[i][j]
                    visited[i][j] = arr[i][j]
        cnt += 1

    print(cnt)

baek16234()
