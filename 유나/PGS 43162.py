def solution(n, computers):
    answer = 0
    from collections import deque
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            que = deque()
            que.append(i)
            
            while que:
                k = que.popleft()
                for idx in range(n):
                    if computers[k][idx] == 1 and visited[idx] == 0:
                        visited[idx] = 1
                        que.append(idx)
            answer += 1
        
    return answer
