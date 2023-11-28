def solution(maps):
    N = len(maps)  # 행
    M = len(maps[0])  # 열

    sx, sy = 0, 0
    ex, ey = 0, 0
    lx, ly = 0, 0
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    
    def bfs_lever(i, j):
        visited = [[0] * M for _ in range(N)]
        q = [(i, j)]
        visited[i][j] = 1
        
        while q:
            x, y = q.pop(0)
            if maps[x][y] == 'L':
                return visited[x][y] - 1
            
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    
    def bfs_door(i, j):
        visited = [[0] * M for _ in range(N)]
        q = [(i, j)]
        visited[i][j] = 1
        
        while q:
            x, y = q.pop(0)
            if maps[x][y] == 'E':
                return visited[x][y] - 1
            
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    lever_cnt = bfs_lever(sx, sy)
    door_cnt = bfs_door(lx, ly)
    
    result = -1
    if lever_cnt != None and door_cnt != None:
        result = lever_cnt + door_cnt

    return result
