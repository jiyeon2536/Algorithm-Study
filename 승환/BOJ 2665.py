def boj2665():
    from collections import deque
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    # 윗줄 맨 왼쪽 방은 항상 흰 방
    # 아랫줄 맨 오른쪽 방은 끝방,
    # 가장 적은 수의 방 색을 바꾸려고 한다.
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[1e9] * n for _ in range(n)]

    # 1일 때 흰 방
    def bfs():
        x = 0
        y = 0
        q = deque()
        q.append((0, 0, 0))
        visited[0][0] = 0
        while q:
            cnt, x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > cnt:
                    if arr[nx][ny] == '1':
                        visited[nx][ny] = cnt
                        q.append((cnt, nx, ny))
                    else:
                        visited[nx][ny] = cnt + 1
                        q.append((cnt + 1, nx, ny))
    bfs()
    print(visited[n-1][n-1])

boj2665()
