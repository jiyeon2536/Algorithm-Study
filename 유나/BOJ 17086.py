from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

# 큐 생성
que = deque()
# 방문 체크 생성
visited = [[0] * m for _ in range(n)]

# 전체 칸 순회하면서 상어가 존재하는 경우
# 큐에 append 및 방문 체크
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            que.append((i, j))
            visited[i][j] = 1

# 최댓값 생성
mx = 0

# bfs, 큐가 있는 동안에 8방탐색
# 최댓값인 경우 갱신
while que:
    k, l = que.popleft()
    for di, dj in [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1, 1],[1,1],[1, -1]]:
        ni, nj = k + di, l + dj
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
            que.append((ni,nj))
            visited[ni][nj] = visited[k][l] + 1
            mx = max(mx, visited[ni][nj])

print(mx - 1)
