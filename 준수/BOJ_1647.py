import heapq

# 열정 MAX
MAX = 100000

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# KRUSKAL을 위한 배열들
min_cost = [MAX] * (N + 1)
visited = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

queue = []

# 1번부터 시작하는 경로를 일단 우선순위 큐에 담는다
for start_cost, start_vertex in graph[1]:
    heapq.heappush(queue, (start_cost, start_vertex))

visited[1] =  1
max_cost = 0
answer = 0

# N-1개의 간선을 선택하는데...
for _ in range(N - 1):
    while queue:
        cost, vertex = heapq.heappop(queue)

        # 이미 선택한 정점이면 skip!
        if visited[vertex]:
            continue
        
        # 아니라면 다음 경로를 우선순위 큐에 추가
        for next_cost, next_vertex in graph[vertex]:
            heapq.heappush(queue, (next_cost, next_vertex))

        # 최소 비용을 총 비용에 더함
        answer += cost
        visited[vertex] = 1

        # 최소 비용 중에 최대값을 구해놓자
        if cost > max_cost:
            max_cost = cost

        break

# 총 비용에서 최대 비용 하나를 제거하면
# 최소 비용으로 만들 수 있는 두 개의 집합을 만들 수 있다
print(answer - max_cost)