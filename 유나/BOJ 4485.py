import heapq
import sys
input = sys.stdin.readline

def dijkstra(si, sj, w):
    # 최단 거리 계산을 위한 dist 생성
    # 첫 번째 인덱스부터 값이 존재하기 때문에 0으로 설정해주지 않앗음
    dist = [[float('inf')] * n for _ in range(n)]
    # 우선순위 que 생성 (w, i, j)
    que = [(w, si, sj)]

    while que:
        # 가중치가 가장 작은 정점 출력
        cur_cost, i, j = heapq.heappop(que)
        # 해당 정점의 가중치가 이미 저장되어 있는 최소값보다 크다면 skip
        if cur_cost > dist[i][j]:
            continue
        # 다음에 이동할 정점 찾기
        for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
            ni, nj = i + di, j + dj
            # 범위 내에 존재하는지 체크
            if 0 <= ni < n and 0 <= nj < n:
                # 다음 정점의 비용 계산
                new_cost = cur_cost + arr[ni][nj]
                # 다음 정점에 저장되어 있는 값이 new_cost보다 크다면,
                # 최소비용 갱신 및 heappush
                if dist[ni][nj] > new_cost:
                    dist[ni][nj] = new_cost
                    heapq.heappush(que, (new_cost, ni, nj))
    return dist[n-1][n-1]

tc = 0
while True:
    tc += 1
    n = int(input().strip()) # 동굴의 크기
    if n == 0:
        break
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    shortest_dist = dijkstra(0, 0, arr[0][0])
    print(f'Problem {tc}: {shortest_dist}')
