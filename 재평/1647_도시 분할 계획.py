import sys
input = sys.stdin.readline

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

edges = []
result = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

for edge in edges:
    cost, A, B = edge

    if find_set(A) != find_set(B):
        union_set(A, B)
        result.append(cost)

print(sum(result[:-1]))