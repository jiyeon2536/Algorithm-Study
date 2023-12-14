import heapq

# 다익스트라 활용
def bfs(start_node, distance, graph, K):
    h = []
    heapq.heappush(h,(0,start_node))
    distance[start_node]=0
    while h:
        dist, node = heapq.heappop(h)
        if distance[node]>dist:
            continue
        for nxt_node,weight in graph[node]:
            if distance[nxt_node]>dist+weight:
                distance[nxt_node] = dist+weight
                heapq.heappush(h, (distance[nxt_node], nxt_node))

    answer = 0
    for dist in distance:
        if dist<=K:
            answer+=1
    return answer
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for v1,v2,w in road:
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    return bfs(1, [float('inf')]*(N+1),graph, K)

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))


# 다익스트라 알고리즘 : 가중치가 있으며, 시작점은 고정, 도착지점은 여러개일때 활용
# 벨만포드 알고리즘 : 가중치가 음수 일때
# 플로이드워셜 알고리즘 : 모든 노드에서 시작할 수 있음. 자신을 제외한 모든 곳에 도달하는데 걸리는 최소비용을 구함.
