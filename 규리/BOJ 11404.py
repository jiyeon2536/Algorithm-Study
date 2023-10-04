import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    check = False
    for x in range(len(graph[u])):
        if graph[u][x][0] == v:
            check = True
            if graph[u][x][1] > w:
                graph[u][x] = (v, w)
    if check == False:
        graph[u].append((v, w))

def floyd_warshall(graph):
    dist = [[float('inf')] * (V+1) for _ in range(V+1)]

    for i in range(V+1):
        dist[i][i] = 0

    for u in range(V+1):
        for v, w in graph[u]:
            dist[u][v] = w

    for k in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

shortest_dist = floyd_warshall(graph)
for i in range(1, len(shortest_dist)):
    for j in range(1, len(shortest_dist[i])):
        if shortest_dist[i][j] == float('inf'):
            shortest_dist[i][j] = 0

for i in range(1, len(shortest_dist)):
    print(*shortest_dist[i][1:])
