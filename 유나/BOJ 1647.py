import sys
input = sys.stdin.readline

# 유니온 파인드
def find(parents, x):
    if x == parents[x]:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    px = find(parents, x)
    py = find(parents, y)
    if px == py:
        return
    if px < py:
        parents[py] = px
    else:
        parents[px] = py

def kruskal(graph):
    edges = [] # 모든 간선 정보가 잇는 리스트
    for u in range(n+1):
        for v, w in graph[u]:
            edges.append((u, v, w))

    # 간선 가중치를 기준으로 오름차순 ㅊ정렬
    edges.sort(key = lambda x:x[2])
    MST = []

    parents = [i for i in range(n+1)]

    for u, v, w in edges:
        if find(parents, u) != find(parents, v):
            MST.append((u, v, w))
            union(parents, u, v)
    return MST

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    # 길이니까 왔다갔다 가능한~
    graph[u].append((v, w))
    graph[v].append((u, w))

MST = kruskal(graph)

# 마을을 두 개로 분할하고자 함 
# MST로 모든 정점을 연결하는 경로를 찾았으므로 최댓값을 빼주면 된다...
total = 0
mx = 0
for u, v, cost in MST:
    total += cost
    mx = max(mx, cost)

print(total - mx)
