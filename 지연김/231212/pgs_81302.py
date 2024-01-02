# 거리두기 확인하기

def solution(places):
    answer = []
    
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    def bfs(r, c, place):
        need_visit = [(r, c)]
        now_visited = [[0] * 5 for _ in range(5)]
        now_visited[r][c] = 1
        
        while need_visit:
            tmp = need_visit.pop(0)
            i = tmp[0]
            j = tmp[1]
            
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                
                if 0 <= ni < 5 and 0 <= nj < 5 and now_visited[ni][nj] == 0:
                    
                    if place[ni][nj] == 'O':
                        now_visited[ni][nj] = now_visited[i][j] + 1
                        need_visit.append((ni, nj))
                        
                    # 다른 P를 만나면
                    if place[ni][nj] == 'P':
                        # 그 P는 아직 visited 값이 없을때만
                        if visited[ni][nj] == 0:
                            # 시작점 P의 전체비짓값을 적어주고 bfs를 종료
                            visited[r][c] = now_visited[i][j]
                            # print(now_visited[i][j])
                            return
                        else:
                            visited[r][c] = 100
                            return

                        
    
    for place in places:
        check = 1
        visited = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    bfs(i, j, place)
                    if visited[i][j] == 0:
                        visited[i][j] = 100
                
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if visited[i][j] < 3:
                        check = 0
        
        answer.append(check)

    return answer