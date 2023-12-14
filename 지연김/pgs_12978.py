# 배달

import heapq
def solution(N, road, K):
    answer = 0
    distance = [float('inf') for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    def dij(start):
        min_heap = [(0, start)]
        distance[start] = 0
        
        while min_heap:
            cur_cost, now = heapq.heappop(min_heap)
            
            if distance[now] < cur_cost:
                continue
            
            for next_node, cost in graph[now]:
                new_cost = cur_cost + cost
                
                if distance[next_node] >= new_cost:
                    distance[next_node] = new_cost
                    heapq.heappush(min_heap, (new_cost, next_node))
        
    dij(1)
    
    for i in distance:
        if i <= K:
            answer += 1
        
        
    return answer