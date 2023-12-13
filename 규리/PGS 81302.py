def solution(places):
    answer = []
    
    def bfs(place, i, j):
        q = [(i, j)]
        visited = [[0]*5 for _ in range(5)]
        visited[i][j] = 1
        
        while q:
            x, y = q.pop(0)
            if (x, y) != (i, j) and place[x][y] == 'P' and visited[x][y] < 4:
                return False
            for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
                nx, ny = x+dx, y+dy
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0 and place[nx][ny] != 'X':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    
    for place in places:
        result = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    res = bfs(place, i, j)
                    if res == False:
                        result = False
        if result == False:
            answer.append(0)
        else:
            answer.append(1)
    
    return answer
