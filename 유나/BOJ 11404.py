import sys
input = sys.stdin.readline

n = int(input().strip()) # 도시의 개수
m = int(input().strip()) # 버스의 개수
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    graph[u-1].append((v-1, w))

def floyd_warshell(graphh):
    # 최소 비용을 계산하는 dist 배열  vxv
    # 약간 인접행렬 만드는 느낌이야
    dist = [[float('inf')] * (n) for _ in range(n)]

    # 자기 자신으로 가는 정점의 최소 비용은 0
    for i in range(n):
        dist[i][i] = 0

    # 인접 리스트에서 모든 간선 정보를 가져와서 최소 비용 갱신
    # u에서 v로 가는 비용 입력
    for u in range(n):
        for v, w in graph[u]:
            if dist[u][v] > w:
                dist[u][v] = w

    # i-k-j 최소 비용으로 계속 갱신을 시도
    # i에서 j 가면서 k 들리는 경우 고려해주기
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # k를 들려서 가면 좀 나을까용?
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

short_dist = floyd_warshell(graph)
# 만약에 갈 수 없는 노드가 있다면 0으로 변경해주기!
for row in short_dist:
    for i in range(n):
        if row[i] == float('inf'):
            row[i] = 0
    print(*row)
