# 무인도 여행
def solution(maps):
    def bfs(i, j):
        total = int(maps[i][j])
        visited[i][j] = True
        need_visit = [(i,j)]
        
        while need_visit:
            tmp = need_visit.pop(0)
            r = tmp[0]
            c = tmp[1]
            for k in range(4):
                nr = r + di[k]
                nc = c + dj[k]
                if 0 <= nr < m and 0 <= nc < n and (not visited[nr][nc]) and maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    total += int(maps[nr][nc])
                    need_visit.append((nr, nc))
        
        return total
        
    answer = []
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    m = len(maps)
    n = len(maps[0])
    
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X' and not visited[i][j]:
                total = bfs(i, j)
                answer.append(total)
                
    answer.sort()
    
    if not answer:
        answer = [-1]
    
    return answer