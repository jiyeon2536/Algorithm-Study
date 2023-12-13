P, W = map(int, input().split())  # 백준과 큐브 - P개의 지점과 W개의 길
C, V = map(int, input().split())  # 백준 수도 C와 큐브 수도 V
graph = [[] for _ in range(P)]

for _ in range(W):
    s, e, w = map(int, input().split())  # 길이 연결하는 두 지점 s, e / 길의 너비 w
    graph[s].append((e, w))
    graph[e].append((s, w))

# 부모 노드를 찾는 함수
def find(parents, x):
    if x == parents[x]:
        return x
    else:
        return find(parents, parents[x])  # 경로압축


# 두 집합을 합치는 함수
def union(parents, x, y):
    # x, y에 대한 부모 찾기
    px = find(parents, x)
    py = find(parents, y)
    if px < py:
        parents[py] = px
    else:
        parents[px] = py


def kruskal(graph):
    edges = []  # 모든 간선 정보가 있는 리스트
    for u in range(P):
        for v, w in graph[u]:
            edges.append((u, v, w))

    edges.sort(key=lambda x:x[2])
    width = []

    parents = [i for i in range(P+1)]  # 각 정점의 부모를 초기화

    while find(parents, C) != find(parents, V):
        u, v, w = edges.pop()
        if find(parents, u) != find(parents, v):
            width.append(w)
            union(parents, u, v) # 두 집합을 합치도록 진행
    return width

result = kruskal(graph)
print(min(result))
