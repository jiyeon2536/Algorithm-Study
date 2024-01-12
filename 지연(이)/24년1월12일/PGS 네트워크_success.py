from collections import deque

def solution(n, computers):
    
    def bfs(v):
        q = deque([v])
        while q:
            v = q.popleft()
            for nv in range(n):
                if computers[v][nv] and not visit[nv]:
                    visit[nv] = 1
                    q.append(nv)
    
    answer = 0    
    visit = [0]*n
    for i in range(n):
        if not visit[i]:
            bfs(i)
            answer+=1

    return answer
