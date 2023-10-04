'''
타임머신 : 벨만 포드 (참고)
1번에서 각 노드로 가는 최소 비용 확인
- 음수 사이클 존재하는지 확인 : 있으면 첫째줄애 -1만 출력
- 해당 도시로 가는 길이 없다면 -1
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
# 간선 정보 입력
edges = []
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    edges.append((u, v, w))

inf = sys.maxsize # 매우 큰 값 생성
def bellman_ford(start):
    # 노드 번호사가 1번부터 시작하므로 n+1
    dist = [inf] * (n+1)
    # 시작노드 = 0
    dist[start] = 0

    # n-1번 순회
    for _ in range(n-1):
        for u, v, w in edges:
            new_cost = dist[u] + w
            # 새로 계산된 값이 기존의 최소비용보다 작다면 갱신
            # dist[u]가 계속 inf이면 이전에 방문한 적이 없다는 것이기 때문...
            if dist[v] > new_cost and dist[u] != inf:
                dist[v] = new_cost

    # 음수 사이클 확인하기 위하여 한 번 더 돌리기!
    # 돌려서 최소비용이라고 생성된 값보다 더 작아진다면....! 음수 사이클 존재
    minus_cycle = False
    for u, v, w in edges:
        if dist[u] != inf and dist[v] > dist[u] + w:
            minus_cycle = True

    return minus_cycle, dist

minus_cycle, short_dist = bellman_ford(1)

# 음수 사이클 존재하지 않는 경우, 방문한적 없는지 체크하고 출력
# 음수 사이클 존재하는 경우, -1만 출력
if not minus_cycle:
    for i in range(2, n+1):
        if short_dist[i] != inf:
            print(short_dist[i])
        else:
            print(-1)
else:
    print(-1)
