def boj16236():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 처음 상어의 크기는 2이다.
    # 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
    # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
    # 먹을 수 있는 물고기가 1마리 이상이면 가장 가까운 물고기를 먹으러 간다.
    # 거리가 가까운 물고기가 여러마리라면 가장 위, 왼쪽 순이다.
    # 아기상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.
    # --> 2인 경우 2마리 먹으면 크기 증가함
    # 0은 빈칸, 1,2,3,4,5,6 칸에 있는 물고기의 크기
    # 9는 아기상어의 위치
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    from collections import deque
    def bfs(start):
        visited = [[0] * N for _ in range(N)]
        nonlocal cnt
        nonlocal size
        eat = []
        chk = True
        q = deque()
        q.append(start)
        visited[start[0]][start[1]] = 1
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                    if arr[nx][ny] <= size:  # 갈 수 있을 때
                        if arr[nx][ny] == 0 or arr[nx][ny] == size:  # 못먹는 경우
                            visited[nx][ny] = visited[x][y] + 1
                            if chk is True:
                                q.append((nx, ny))
                        elif arr[nx][ny] < size:  # 먹는 경우
                            if (nx, ny) in eat:
                                continue
                            visited[nx][ny] = visited[x][y] + 1
                            eat.append((visited[nx][ny], nx, ny))
                            chk = False
        if len(eat) >= 1:
            eat.sort(key=lambda x:(x[0], x[1], x[2]))
            return eat[0][0], eat[0][1], eat[0][2]
        else:
            return 0, 0, 0

    cnt = 0
    size = 2
    size_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                start = (i, j)
                break
    while True:
        ans, rx, ry = bfs(start)
        arr[rx][ry] = 0
        if ans > 0:
            start = (rx, ry)
            size_cnt += 1
            if size_cnt == size:
                size_cnt = 0
                size += 1
            cnt += ans-1
        else:
            break
    print(cnt)


boj16236()
