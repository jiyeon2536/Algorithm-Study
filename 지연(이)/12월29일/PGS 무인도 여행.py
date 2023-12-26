from collections import deque

    

def solution(maps):
    answer = []
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    N = len(maps)
    M = len(maps[0])
    visit = [[False]*M for _ in range(N)]
    
    def bfs(x,y):
        visit[x][y]=True
        q = deque([(x,y)])
        value = int(maps[x][y])
        while q:
            x,y = q.popleft()
            for dx,dy in d:
                nx = x + dx
                ny = y + dy
                if 0<=nx<N and 0<=ny<M and maps[nx][ny]!='X' and not visit[nx][ny]:
                    q.append((nx,ny))
                    value += int(maps[nx][ny])
                    visit[nx][ny]=True
        
        return value
    
    for x in range(N):
        for y in range(M):
            if maps[x][y]!="X" and not visit[x][y]:
                value = bfs(x,y)
                if value:
                    answer.append(value)
    answer.sort()
    if not answer:
        answer = [-1]
    return answer
