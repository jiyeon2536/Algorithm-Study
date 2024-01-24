from collections import deque
d = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x, y, N, M, land):
    q = deque([(x,y)])
    cnt = 1
    land[x][y]=0
    col = {y}
    while q:
        x, y = q.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and land[nx][ny]:
                land[nx][ny]=0
                cnt+=1
                col.add(ny)
                q.append((nx,ny))

    return col, cnt

def solution(land):
    N = len(land)
    M = len(land[0])
    col = [0]*M

    for i in range(N):
        for j in range(M):
            if land[i][j]:
                lst, val = bfs(i, j, N, M, land)
                for c in lst:
                    col[c]+=val
    return max(col)

