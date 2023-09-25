def binary_search(low, high):
    result = -1

    # Binary Search
    while low <= high:
        mid = (low + high) // 2

        # mid 이하의 weight를 가진 간선만 지날 수 있을 경우
        is_possible = bfs(mid)

        # 도착할 수 있는 경우
        if is_possible:
            # result에 mid 값을 저장하고
            result = mid
            # 더 작은 mid 값을 찾기 위해 high 값을 조정
            high = mid - 1
        else:
            # 도착 가능한 mid 값을 찾기 위해 low 값을 조정
            low = mid + 1

    # 모든 값에 대해 도착할 수 없다면 -1
    # 도착할 수 있다면 최소값을 반환
    return result


# A 정점에서 출발하여 B 정점에 도착했을 때 비용이 C 이하인가?
# max_cost: binary search를 통해 전달한 인자
def bfs(max_cost):
    min_cost = [MAX] * (N + 1)
    min_cost[A] = 0
    queue = [(0, A)]

    while queue:
        cost, vertex = heapq.heappop(queue)

        # 도착하기 전에 최대 비용을 초과하면 prunning
        if cost > C:
            continue
        
        # 현재 경로가 최선이 아닌 경우 prunning 
        if cost > min_cost[vertex]:
            continue

        for next_cost, next_vertex in graph[vertex]:
            # binary search로 찾은 값보다 간선의 weight가 크면 skip
            if next_cost > max_cost:
                continue

            if min_cost[next_vertex] > min_cost[vertex] + next_cost:
                min_cost[next_vertex] = min_cost[vertex] + next_cost
                heapq.heappush(queue, (min_cost[next_vertex], next_vertex))

    # 도착점으로 이어진 간선들이 있고
    # 도착까지 필요한 비용이 C 이하일 경우
    if min_cost[B] <= C:
        return True
    else:
        return False


import heapq

# 각 간선들의 최대 비용 * 노드의 수
MAX = int(1e16)
N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    S, E, W = map(int, input().split())

    graph[S].append([W, E])
    graph[E].append([W, S])

answer = binary_search(0, int(1e9))
print(answer)