import sys
input = sys.stdin.readline

def bfs(x, y):
    global visited
    arr = []  # 연합 칸 좌표
    total = 0  # 연합 인구 수
    queue = [(x, y)]

    while queue:
        i, j = queue.pop(0)
        for di, dj in [0, 1], [1, 0], [-1, 0], [0, -1]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and L <= abs(A[i][j] - A[ni][nj]) <= R:
                visited[ni][nj] = True
                total += A[ni][nj]
                arr.append((ni, nj))
                queue.append((ni, nj))
    
    length = len(arr)  # 연합 칸 수
    if length > 0:
        v = total // length  # 각 칸 인구 수
        for i, j in arr:
            A[i][j] = v
    return length

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    visited = [[False] * N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                res = bfs(i, j)
                result += res
    if result == 0:  # 연합 칸 없으면(인구이동 x) break
        break
    ans += 1
print(ans)
