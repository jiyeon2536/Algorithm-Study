from collections import deque

def solution(n, wires):
    def bfs(visit, x, y):
        q = deque([x])
        visit[x] = 1
        while q:
            x = q.popleft()
            for nx in graph[x]:
                if not visit[nx] and nx != y:
                    q.append(nx)
                    visit[nx]=1
        cnt = 0
        for i in range(1,n+1):
            if visit[i]==1:
                cnt+=1
        return abs(n-cnt-cnt)
    
    
    
    answer = float('inf')
    
    graph = [[] for _ in range(n+1)]
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    
    for x,y in wires:
        visit = [0]*(1+n)
        tmp = bfs(visit, x, y)
        answer = min(answer, tmp)
    
    return answer
