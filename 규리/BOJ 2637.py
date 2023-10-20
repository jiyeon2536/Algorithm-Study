from collections import deque

# # 1~(N-1):기본부품, 중간부품 번호 / N:완제품번호
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
outdegree = [0]*(N+1)
arr = [0]*(N+1)

for _ in range(M):
    # X를 만드는데 Y가 K개 필요
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))
    indegree[X] += 1
    outdegree[Y] += 1

q = deque()
ans = []
for i in range(1, N+1):
    if indegree[i] == 0:
        ans.append(i)
    if outdegree[i] == 0:
        arr[i] = 1
        q.append(i)

while q:
    u = q.popleft()
    for v, k in graph[u]:
        arr[v] += arr[u] * k
        outdegree[v] -= 1
        if outdegree[v] == 0:
            q.append(v)

# 처음 진입차수 0인 것만 출력
for i in ans:
    print(i, arr[i])
