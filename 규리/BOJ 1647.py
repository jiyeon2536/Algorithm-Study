import heapq, sys
input = sys.stdin.readline

def prim(start):
    visited = [False] * (N+1)
    min_heap = [(0, start)]
    MST = []

    while min_heap:
        # 유지비 가장 작은 길 추출
        cost, home = heapq.heappop(min_heap)
        # 방문했으면 continue
        if visited[home]:
            continue
        visited[home] = True
        MST.append((home, cost))
        for nxt, cost in graph[home]:
            if not visited[nxt]:
                heapq.heappush(min_heap, (cost, nxt))
    return MST

N, M = map(int, input().split())  # 집의 개수 N, 길의 개수 M
graph = [[] for _ in range(N+1)]
for _ in range(M):
    # A번 - B번 집 연결하는 유지비 C
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start = 1
MST = prim(start)

MST.sort(key=lambda x:x[1])  # 비용 작은순 정렬
MST.pop()  # 최대 비용 pop

total = 0
for home, cost in MST:
    total += cost
print(total)
