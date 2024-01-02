# 마법의 엘리베이터
from collections import deque 

def solution(storey):
    answer = 0
    def bfs(storey):
        visited[storey] = 1
        need_visit = deque()
        need_visit.append(storey)
        while need_visit:
            now = need_visit.popleft()
            if now == 0:
                return 
            for i in range(16):
                if i <= 7:
                    nxt = now + (10 ** i)
                elif i > 7:
                    nxt = now - (10 ** (i - 8))
                if 0 <= nxt <= 100000000 and visited[nxt] == 0:
                    visited[nxt] = visited[now] + 1
                    need_visit.append(nxt)
            
            
    visited = [0 for _ in range(100000001)]
    bfs(storey)
    answer = visited[0] - 1 
    
    return answer