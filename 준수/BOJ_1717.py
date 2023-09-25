def union(parent, child):
    # 가장 높은 부모 노드 번호를 가져옴
    parent = find(parent)
    child = find(child)

    # 작은 노드 번호로 부모 번호를 통합
    if parent < child:
        super_shy[child] = parent
    else:
        super_shy[parent] = child

def find(node):
    # 자신의 부모 노드 번호와 자신의 번호가 같으면
    if super_shy[node] == node:
        # 내가 바로 루트 노드
        return node
    
    # 자신이 루트 노드가 아니라면
    if super_shy[node] != node:
        # 가장 위의 부모 노드... 즉 루트 노드를 할당
        super_shy[node] = find(super_shy[node])

    # 그 위의 부모 노드를 찾는다
    return super_shy[node]

import sys
input = sys.stdin.readline
# 재귀 리미트 해제!
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
# 자신의 부모 노드는 자신으로 표시
super_shy = [x for x in range(N + 1)]

for _ in range(M):
    cmd, a, b = map(int, input().split())

    # union
    if cmd == 0:
        union(a, b)
    # find
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')