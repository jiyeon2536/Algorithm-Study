# 네트워크
def solution(n, computers):
    answer = 0

    adj = [[0] for _ in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                adj[i].append(j)
                adj[j].append(i)
        
    visited = [False] * (n+1)

    
    def dfs(first): 
        nonlocal answer
        answer += 1
        stack = [first]
        while stack:
            current = stack.pop()
            for i in adj[current]:
                if visited[i] == False:
                    visited[i] = True
                    stack.append(i)
        return
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            
            
    return answer