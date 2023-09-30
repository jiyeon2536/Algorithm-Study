import sys
input = sys.stdin.readline

# 최단 거리로 돌아 수색 범위내에 방문할 수 있는지를 체크  ->  가져올 수 있는 아이템 수 계산
def floyd_warshell():
    dist = [[inf] * (n) for _ in range(n)]

    # 자기 자신으로 가는 것은 0으로 맞춰주기
    for i in range(n):
        dist[i][i] = 0

    # u-v 인접 리스트에서 모든 간선 정보 가져와 최소 비용 갱신
    for u in range(n):
        for v, w in graph[u]:
            if dist[u][v] > w:
                dist[u][v] = w

    # i-k-j 돌면서 최솟값 갱신하기
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# 지역 개수, 수색 범위, 길의 개수
n, m, r = map(int, input().strip().split())
items = list(map(int, input().strip().split())) # 각 구역의 아이템 수

# 인접 리스트 생성
graph = [[] for _ in range(n)]
for _ in range(r):
    u, v, w = map(int, input().strip().split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

inf = sys.maxsize
short_dist = floyd_warshell()

# 아이템의 최댓값
mx = 0
# 각 출발지별로 순회하면서 total 값이 최대인 경우 갱신
for i in range(n):
    total = 0
    for j in range(n):
        if short_dist[i][j] <= m:
            total += items[j]
    mx = max(mx, total)

print(mx)
