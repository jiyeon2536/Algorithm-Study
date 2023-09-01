dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(i, j, color):
    q = [(i, j)]
    visited[i][j] = 1
    global sv
    while q:
        x, y = q.pop()
        sv += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return sv

N, M = map(int, input().split())
# N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 다만 대각선으로만 인접한 경우는 x
# bfs로 풀자 그냥
visited = [[0] * N for _ in range(M)]
arr = [list(input()) for _ in range(M)]
sv = 0
svB = 0
svW = 0
for i in range(M):
    for j in range(N):
        sv = 0
        if visited[i][j] == 0:
            if arr[i][j] == 'B':
                svB += bfs(i, j, arr[i][j]) ** 2
            else:  # 'W'일 때
                svW += bfs(i, j, arr[i][j]) ** 2
print(svW, svB)
