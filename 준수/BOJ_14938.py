import heapq

def bfs(start):
    mn_dist = [float('inf')] * (N + 1)
    mn_dist[start] = 0
    mx_item = [0] * (N + 1)
    mx_item[start] = items[start]
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, vertex = heapq.heappop(queue)

        for next_dist, next_vertex in graph[vertex]:
            if next_dist + mn_dist[vertex] > M:
                continue

            if mn_dist[next_vertex] > mn_dist[vertex] + next_dist:
                mn_dist[next_vertex] = mn_dist[vertex] + next_dist
                mx_item[next_vertex] = items[next_vertex]
                heapq.heappush(queue, (mn_dist[next_vertex], next_vertex))

    return sum(mx_item)

N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(R):
    a, b, l = map(int, input().split())

    if l <= M:
        graph[a].append((l, b))
        graph[b].append((l, a))

answer = 0

for node in range(1, N + 1):
    result = bfs(node)

    if result > answer:
        answer = result

print(answer)