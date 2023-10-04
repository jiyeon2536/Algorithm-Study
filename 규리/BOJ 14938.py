import heapq, sys
input = sys.stdin.readline

n, m, r = map(int, input().split())  # n:지역개수 / m:수색범위 / r:길의개수
item = [0] + list(map(int, input().split()))  # n개의 숫자가 차례대로 각 구역에 있는 아이템의 수
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())  # 길 양 끝 지역번호 a, b / 길의 길이 l
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(graph, start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    mn = [(0, start)]

    while mn:
        cur_len, node = heapq.heappop(mn)
        if cur_len > dist[node]:
            continue

        for nxt, length in graph[node]:
            new_len = cur_len + length
            if dist[nxt] > new_len:
                dist[nxt] = new_len
                heapq.heappush(mn, (new_len, nxt))
    return dist

mx = 0
# 낙하지점 찾기
for start in range(1, n+1):
    result = 0
    arr = dijkstra(graph, start)

    for i in range(1, n+1):
        if arr[i] <= m:  # 수색범위 안에 드는지
            result += item[i]
    mx = max(result, mx)  # 최대값 갱신

print(mx)
