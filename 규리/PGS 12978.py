import heapq

def solution(N, road, K):
    answer = 1
    graph = [[] for _ in range(N+1)]
    for x, y, t in road:
        graph[x].append((y, t))
        graph[y].append((x, t))
    
    def deliver(graph):
        q = [(1, 0)]  # 마을번호, 시간
        times = [float('inf')]*(N+1)
        times[1] = 0
        
        while q:
            cur, cur_time = heapq.heappop(q)
            
            if cur_time > times[cur]:
                continue
            
            for nxt, nxt_time in graph[cur]:
                new_time = cur_time + nxt_time
                if times[nxt] > new_time:
                    times[nxt] = new_time
                    heapq.heappush(q, (nxt, new_time))
                
        return times

    times = deliver(graph)
    print(times)
    for time in times[2:]:
        if 0 < time <= K:
            answer += 1

    return answer
