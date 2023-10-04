import sys
input = sys.stdin.readline

def floyd():
    cost = [[float('inf')] * N for _ in range(N)]

    # 자기자신으로 가는 비용은 0 원
    for _ in range(N):
        cost[_][_] = 0
    # 입력에서 같은 노선이라도 더 낮은 비용이 주어질 수 있으므로
    # 각 도시에서 다른 도시로 가는 현재의 직통 최저 비용 정보를 저장
    for node in range(1, N + 1):
        for next, c in graph[node]:
            if cost[node - 1][next - 1] > c:
                cost[node - 1][next - 1] = c

    # 각 도시에서 또다른 도시로 바로 가는것 보다 연결되어 있는 도시들을 순회하여
    # 더 낮은 비용으로 갈 수 있다면 최소비용을 갱신 
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if cost[b][c] > cost[b][a] + cost[a][c]:
                    cost[b][c] = cost[b][a] + cost[a][c]

    return cost

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

res = floyd()

for q in range(N):
    for p in range(N):
        if res[q][p] == float('inf'):
            res[q][p] = 0
    print(*res[q])
