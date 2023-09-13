# 토마토
from collections import deque
import sys
input = sys.stdin.readline

# bfs
def bfs():
    global mn
    while que:
        i, j= que.popleft()
        # 상하좌우가 범위 내이고, 안익은 토마토이고, 방문한 적이 없다면 que에 입력
        for di, dj in [[0,1], [0, -1], [1,0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m  and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                que.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1


# 열, 행
m, n = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

# 익은 토마토들 동시에 돌리기 위해 미리 que에 입력, 방문 체크열에도 체크
que = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            que.append((i, j))
            visited[i][j] = 1

bfs()

ans = 0
# 안익은 토마토이면서, 방문체크열에 0인 경우 체크 - 있으면 -1 출력, 있으면 최댓값-1 출력
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and arr[i][j] == 0:
            ans = -1
            break
        else:
            ans = max(ans, visited[i][j]-1)
    if ans == -1:
        break

print(ans)
