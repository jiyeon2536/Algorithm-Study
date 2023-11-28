def find(z):
    if parent[z] == z:
        return z

    parent[z] = find(parent[z])
    return parent[z]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


p, w = map(int, input().split())
c, v = map(int, input().split())

edges = []
parent = [_ for _ in range(p)]
visited = [False] * p

for _ in range(w):
    s, e, w = map(int, input().split())
    edges.append([w, s, e])

answer = 1001
edges.sort(key=lambda x: x[0], reverse=True)

graph = [[] for _ in range(p)]
route = [int(1e9)] * p
visited = [False] * p
queue = [c]
visited[c] = True

while edges:
    cost, start, end = edges.pop(0)

    if find(start) != find(end):
        union(start, end)
        graph[start].append([cost, end])
        graph[end].append([cost, start])

while queue:
    vertex = queue.pop()

    for next_cost, next_vertex in graph[vertex]:
        if visited[next_vertex] == False:
            visited[next_vertex] = True
            route[next_vertex] = min(next_cost, route[vertex])
            queue.append(next_vertex)

print(route[v])
