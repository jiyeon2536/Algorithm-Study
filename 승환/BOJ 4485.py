def baek4485():
    import heapq
    tc = 0
    while True:
        tc += 1
        N = int(input())
        if N == 0:
            break
        arr = [list(map(int, input().split())) for _ in range(N)]
        distance = [[float('inf')] * N for _ in range(N)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        hq = [(arr[0][0], 0, 0)]  # 출발점
        while hq:
            weight, x, y = heapq.heappop(hq)
            if distance[x][y] < weight:
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and distance[nx][ny] == float('inf'):
                    n_weight = weight + arr[nx][ny]
                    # 기존 값보다 클경우 제외
                    if distance[nx][ny] <= n_weight:
                        continue
                    distance[nx][ny] = n_weight
                    heapq.heappush(hq, (n_weight, nx, ny))
        print(f'Problem {tc}: {distance[N-1][N-1]}')

baek4485()
