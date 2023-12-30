def solution(grid):
    direction = [(0,1),(-1,0),(0,-1),(1,0)]
    def dfs(x,y,d):
        move = 0
        while True:
            nx = (x + direction[d][0])%N
            ny = (y + direction[d][1])%M

            if grid[nx][ny]=='L':
                d = (d+1)%4
            elif grid[nx][ny]=='R':
                d = (d-1)%4
            
            if not visit[nx][ny][d]:
                visit[nx][ny][d]=1
                x,y = nx,ny
                move+=1
            else:
                return move
    
    answer = []
    
    N = len(grid)
    M = len(grid[0])
    visit = [[[0]*4 for _ in range(M)] for _ in range(N)]
    
    for x in range(N):
        for y in range(M):
            for d in range(4):
                if not visit[x][y][d]:
                    move = dfs(x,y,d)
                    if move:
                        answer.append(move)
    answer.sort()
    return answer
