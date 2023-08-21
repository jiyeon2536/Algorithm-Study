import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    if 0 <= i < N and 0 <= j < M:
        if box[i][j] == 1:
            box[i][j] = 0
            for k in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                x, y = k
                dfs(x, y)
            return True
        return False
    else:
        return False

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())  # 가로 / 세로 / 배추위치개수
    box = [[0]*M for _ in range(N)]
    for _ in range(K):
        b, a = map(int, input().split())  # 가로, 세로 -> box[a][b]
        box[a][b] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1

    print(result)
