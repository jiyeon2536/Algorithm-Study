from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)


for _ in range(M):
    A, B = map(int, input().split())
    in_degree[B] += 1
    graph[A].append(B)
visited = [False] * (N + 1)

deq = deque()

ans = []

i = 0

for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        deq.append(i)
        visited[i] = True

while deq:
    n = deq.popleft()
    ans.append(n)
    for j in graph[n]:
        if visited[j] == False:

            in_degree[j] -= 1
            if in_degree[j] == 0:
                deq.append(j)
                visited[j] = True

print(*ans)

"""
위상정렬
비순환 방향 그래프 ( 사이클이 없고 방향성이 존재 ) 에서 정점을 선형으로 정렬
모든 간선 (u, v) 에 대해서 정점 u 가 정점 v 보다 먼저 오는 순서로 정렬이 된다.

무방향
degree : 하나의 정점에 인접한 정점의 수

방향
in_degree : 외부 노드에서 들어오는 간선의 수
out_degree : 한 노드에서 외부로 향하는 간선의 수

BFS 를 이용하여 위상정렬
1. 모든 정점의 진입차수 (in_degree) 를 설정
2. in_degree 가 0 인 정점은 방문한 것으로 표시하고 큐에 정점을 추가
3. 큐가 빌 때 까지 순회하며 다음 작업을 수행
3-1. 큐의 앞 요소를 dequeue() 로 가져와 T[] 에 append
3-2. dequeue() 의 한 정점에 인접한 정점 중 방문하지 않은 정점의 in_degree 를 하나 감소
3-3. in_degree 감소 후 값이 0 이면 해당 정점은 queue 에 enqueue() 하고 방문한 것으로 표시
"""