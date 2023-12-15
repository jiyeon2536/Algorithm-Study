import heapq
def solution(N, road, K):
    answer = 0
    # 1번에서 출발해서 N 개의 마을 중에 K 시간 이하로 배달이 가능한 마을에서만 주문
    graph = [[] for _ in range(N + 1)]
    for i in road:
        s, e, w = i[0], i[1], i[2]
        graph[s].append([e, w])
        graph[e].append([s, w])
    print(graph)
    dist = [int(1e9)] * (N + 1)

    def dijkstra(start):
        pq = []
        heapq.heappush(pq, (0, start))
        dist[start] = 0
        while pq:
            wgt, now = heapq.heappop(pq)
            if dist[now] < wgt:
                continue
            for nxt in graph[now]:
                next_node = nxt[0]
                cst = nxt[1]

                new_cst = wgt + cst
                if dist[next_node] <= new_cst:
                    continue
                dist[next_node] = new_cst
                heapq.heappush(pq, (new_cst, next_node))

    dijkstra(1)
    for i in dist:
        if i <= K:
            answer += 1
    return answer
