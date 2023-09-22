# 경로 압축 find
def find(elem):
    if parent[elem] == elem:
        return elem

    parent[elem] = find(parent[elem])
    return parent[elem]

# union
def union(elem1, elem2):
    elem1 = find(elem1)
    elem2 = find(elem2)

    # 더 작은 노드 번호로 할당
    if elem1 > elem2:
        parent[elem1] = elem2
    else:
        parent[elem2] = elem1

# 정렬을 위한 힙
import heapq

N, E = map(int, input().split())
edges = []
parent = [child for child in range(N + 1)]
total = 0

for _ in range(E):
    n1, n2, w = map(int, input().split())
    # w 값을 기준으로 정렬
    heapq.heappush(edges, (w, n1, n2))

while edges:
    # edges 힙에서 하나씩 popleft
    weight, start, end = heapq.heappop(edges)

    # 같은 부모가 아닌 경우
    # 경로를 연결하면서 최소 비용을 total에 추가
    if find(start) != find(end):
        total += weight
        union(start, end)

print(total)