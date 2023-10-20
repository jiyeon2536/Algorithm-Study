from collections import deque

N = int(input())
M = int(input())

# 인접 행렬
graph = [[0] * (N + 1) for _ in range(N + 1)]
preceding = [0] * (N + 1)

# 리프 노드 확인용
leaf = [0] * (N + 1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[X][Y] = K
    preceding[Y] += 1
    # 리프 노드 확인용
    leaf[X] += 1

made = [0] * (N + 1)
queue = deque()

for n in range(1, N + 1):
    if not preceding[n]:
        queue.append(n)
        made[n] = 1

while queue:
    vertex = queue.popleft()

    for next_vertex in range(1, N + 1):
        if graph[vertex][next_vertex] == 0:
            continue
        
        if preceding[next_vertex] > 0:
            preceding[next_vertex] -= 1
            made[next_vertex] += made[vertex] * graph[vertex][next_vertex]
            graph[vertex][next_vertex] = 0
        else:
            continue

        if preceding[next_vertex] == 0:
            queue.append(next_vertex)
        else:
            queue.append(vertex)

# 리프 노드가 뭐였지?
for n in range(1, N + 1):
    if leaf[n] == 0:
        print(n, made[n])
