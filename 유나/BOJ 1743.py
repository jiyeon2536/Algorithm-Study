import sys
sys.setrecursionlimit(10000) # 재귀 최대 깊이 조정 1000 -> 10000

def dfs(x, y):
    global cnt, visited
    visited[x][y] = 1 # 방문체크
    cnt += 1 # 함수 실행시마다 +1

    # 상하좌우 탐색
    for di, dj in [[0,1], [0,-1], [1,0],[-1,0]]:
        ni = x + di
        nj = y + dj
        # ni nj가 범위내에 있고 방문한 적 없으며, 움식물 쓰레기가 있다면...
        if 0 <= ni < n+1 and 0 <= nj < m+1 and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            dfs(ni, nj)

n, m, k = map(int, input().split())
arr = [[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
    i, j = map(int, input().split())
    arr[i][j] = 1

visited = [[0] * (m+1) for _ in range(n+1)]

# 최댓값
mx = 0
# 모든 인덱스를 순회
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt = 0 # 음식물 쓰레기 더미 count
        # 방문한 적이 없고, 음식물 쓰레기가 존재한다면
        if visited[i][j] == 0 and arr[i][j] == 1:
            dfs(i, j)
            mx = max(cnt, mx) # dfs 탐색 후 cnt가 mx보다 크다면 갱신
print(mx)
