import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
assemble = [[] for _ in range(N + 1)]
parts = [[0] * (N + 1) for _ in range(N + 1)]
queue = deque()
in_degree = [0] * (N+1)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    assemble[b].append((a, c))
    in_degree[a] += 1

for i in range(1, N + 1):
    if not in_degree[i]:
        queue.append(i)

while queue:
    in_progress = queue.popleft()
    for joint, cnt in assemble[in_progress]:
        if parts[in_progress].count(0) == N + 1:
            parts[joint][in_progress] += cnt
        else:
            for i in range(1, N + 1):
                parts[joint][i] += parts[in_progress][i] * cnt
        in_degree[joint] -= 1
        if in_degree[joint] == 0:
            queue.append(joint)
for result in enumerate(parts[N]):
    if result[1] > 0:
        print(*result)