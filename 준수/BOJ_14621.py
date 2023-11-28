def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


N, M = map(int, input().split())
university = [' '] + input().split()
parent = [_ for _ in range(N + 1)]
edges = []

for _ in range(M):
    u, v, d = map(int, input().split())
    edges.append((u, v, d))

edges.sort(key=lambda edge: edge[2])

connected_num = 0
route_len = 0

for start, end, dist in edges:
    if find(start) == find(end) or university[start] == university[end]:
        continue

    union(start, end)
    connected_num += 1
    route_len += dist

if connected_num == N - 1:
    print(route_len)
else:
    print(-1)