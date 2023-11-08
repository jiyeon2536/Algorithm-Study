arr = list(map(int, input().split()))
# 이동횟수, 확률
N, dir = arr[0], [arr[i]/100 for i in range(1, 5)]
visited = [[False]*29 for _ in range(29)]
result = 0

#     동 서  남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# [x][y], 이동횟수, 확률
def dfs(x, y, move, p):
    global result
    visited[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if visited[nx][ny] == False:
            if move == N:  # N번 이동한 경우
                result += p * dir[k]  # 확률을 더함
            else:
                dfs(nx, ny, move+1, p * dir[k])
    visited[x][y] = False

dfs(14, 14, 1, 1)  # 시작점 : 중앙
print(result)
