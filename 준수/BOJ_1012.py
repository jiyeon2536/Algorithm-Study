import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    for dx, dy in [1, 0], [-1, 0], [0, 1], [0, -1]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < M and 0 <= ny < N and dp[nx][ny] == 1:
            # 인접한 배추들은 추가적인 지렁이가 필요없음
            dp[nx][ny] = 0
            dfs(nx, ny)


T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    # 배추밭
    dp = [[0 for _ in range(N)] for _ in range(M)]
    
    # 배추흰지렁이가 필요한 마리 수
    cnt = 0

    # 지렁이의 위치 표시
    for k in range(K):
        x, y = map(int, input().split())
        dp[x][y] = 1

    for i in range(M):
        for j in range(N):
            # 지렁이가 있다면 인접한 배추들을 탐색
            if dp[i][j] == 1:
                cnt += 1
                dp[i][j] = 0
                dfs(i, j)
                
    print(cnt)