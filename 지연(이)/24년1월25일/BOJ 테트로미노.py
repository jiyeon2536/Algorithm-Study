d = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y,depth, value):
    global answer
    if depth==3:
        answer = max(answer, value)
        return
    for dx,dy in d:
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
            if depth==1:
                visit[nx][ny]=1
                dfs(x, y, depth+1, value+arr[nx][ny])
                visit[nx][ny]=0
            visit[nx][ny] = 1
            dfs(nx, ny, depth+1, value+arr[nx][ny])
            visit[nx][ny] = 0

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i,j,0, arr[i][j])
        visit[i][j] = 0

print(answer)
