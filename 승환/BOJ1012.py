import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:  # 범위 내에 가지 않은 곳이 있다면
            arr[nx][ny] = 0  # 체크한 곳 표시
            dfs(nx, ny)


def bfs(x, y):  # bfs로 풀면 시간 초과 발생함??!
    arr[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q.append((x, y))
    while q:
        x, y = q.pop(0)
        arr[x][y] = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= ny < M and 0 <= nx < N and arr[nx][ny] == 1:
                q.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1  # 치사하다
    res = 0
    q = []
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:  # 1을 발견 하면
                dfs(x, y)
                res += 1
    print(res)
'''
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
'''