import sys
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x]) # 경로 압축
    return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        parents[py] = px

n = int(input().strip()) # 도시의 수
m = int(input().strip()) # 여행 계획에 속한 도시들의 수 M

# 인접 행렬
arr = [list(map(int, input().strip().split())) for _ in range(n)]

# 여행 계획 : 부모 노드가 동일한가..?
trip = list(map(int, input().strip().split()))

# 도시 번호가 1부터 n까지
parents = [i for i in range(n+1)]

# 인접 행렬을 순회하면서
# 연결되어 있다면 union으로 묶어줌
for v in range(n):
    for node in range(n):
        if arr[v][node] == 1:
            union(v+1, node+1)

# 도시의 조상 노드가 동일한지 체크
ans = 'YES'
for idx in range(len(trip)-1):
    if find(trip[idx]) != find(trip[idx+1]):
        ans = 'NO'

print(ans)
