from collections import deque

N, M = map(int, input().split())

preceding = [0] * (N + 1)
taller = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    taller[A].append(B)
    preceding[B] += 1

answer = []
queue = deque()

for num in range(1, N + 1):
    if not preceding[num]:
        queue.append(num)

while queue:
    vertex = queue.popleft()

    if preceding[vertex] == 0:
        if not visited[vertex]:
            answer.append(vertex)
            visited[vertex] = True

        for next_vertex in taller[vertex]:
            preceding[next_vertex] -= 1

            if preceding[next_vertex] == 0:
                queue.append(next_vertex)

print(*answer)