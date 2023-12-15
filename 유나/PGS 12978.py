def solution(N, road, K):
    answer = 0
    from collections import deque
    import sys
    inf = sys.maxsize
    # N : 마을 개수, road : 소요 시간 정보, K 소요시간
    
    graph = [[] for _ in range(N+1)]
    visited = [0, 0]+ [inf] * (N-1)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    que = deque()
    que.append((1,0))
    
    while que:
        current, val = que.popleft()
        
        for nxt, nxt_val in graph[current]:
            if val + nxt_val < visited[nxt]:
                que.append((nxt, val + nxt_val))
                visited[nxt] = val + nxt_val
    
    for i in visited:
        if 0 < i <= K:
            answer += 1
    print(visited)

    return answer + 1
