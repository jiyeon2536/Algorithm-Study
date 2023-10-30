import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 진입차수 배열
in_degree = [0] * (N+1)
queue = deque()

for _ in range(M):
    A, B = map(int, input().split())
    in_degree[B] += 1
    graph[A].append(B)

for i in range(1, N+1):
    if not in_degree[i]:
        queue.append(i)

ans = []
while queue:
    number = queue.popleft()
    ans.append(number)
    for i in graph[number]:
        in_degree[i] -= 1
        if not in_degree[i]:
            queue.append(i)
    print(number, end=' ')