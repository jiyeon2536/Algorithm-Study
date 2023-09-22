# 경로 압축 find 함수
def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

# union 함수
def union(x, y):
    x = find(x)
    y = find(y)

    # 중복 방문이 아닌 경우
    if x != y:
        parent[y] = x

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [child for child in range(N + 1)]
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

for i in range(N):
    for j in range(i, N):
        # i에서 j로 갈 수 있는 경로가 있다면
        if adj_matrix[i][j] == 1:
            # 경로가 이어져 있음을 기록
            # 어떤 경우에서도 i가 j보다 작거나 같음
            union(i + 1, j + 1)

is_possible = True
# 시작 도시 지점
root = find(plan[0])

# 가고 싶은 도시의 인덱스가 같은 집합인지 판별
for city in plan:
    if find(root) != find(city):
        is_possible = False
        break

if is_possible:
    print('YES')
else:
    print('NO')