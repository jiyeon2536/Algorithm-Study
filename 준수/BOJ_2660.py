N = int(input())
graph = [[int(1e9)] * N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

while True:
    u, v = map(int, input().split())

    if u == v == -1:
        break

    graph[u - 1][v - 1] = 1
    graph[v - 1][u - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = []
min_score = int(1e9)

for i in range(N):
    score = max(graph[i])

    if min_score > score:
        min_score = score
        ans = [i + 1]
    elif min_score == score:
        ans.append(i + 1)

print(min_score, len(ans))
print(*ans)