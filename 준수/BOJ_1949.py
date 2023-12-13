def dfs(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

            dp[node][1] += dp[next_node][0]
            dp[node][0] += max(dp[next_node][0], dp[next_node][1])

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())

people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
dp = [[0, people[num]] for num in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(max(dp[1]))