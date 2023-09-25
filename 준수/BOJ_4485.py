def bfs():
    # 이동할 때 필요한 최소 비용을 기록할 임시 배열
    cost_matrix = [[MAX] * N for _ in range(N)]
    cost_matrix[0][0] = cave[0][0]
    queue = [(0, 0, 0)]

    # 다익스트라
    while queue:
        cost, x, y = heapq.heappop(queue)

        if cost > cost_matrix[x][y]:
            continue

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]

            if 0 <= nx < N and 0 <= ny < N:
                # 이미 기록해둔 최소 비용과 새로운 경로에서 갱신되는 비용을 비교
                if cost_matrix[nx][ny] > cost_matrix[x][y] + cave[nx][ny]:
                    cost_matrix[nx][ny] = cost_matrix[x][y] + cave[nx][ny]
                    # 다음 경로들도 최소 비용이 바뀔 수 있으므로 갱신
                    heapq.heappush(queue, (cost_matrix[nx][ny], nx, ny))

    # 그래서 젤다가 누구라고?
    return cost_matrix[N - 1][N - 1]


import heapq

# MAX 값 설정
MAX = 125 * 125 * 9

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tc = 1

while True:
    N = int(input())

    if N == 0:
        break
    
    cave = [list(map(int, input().split())) for _ in range(N)]
    result = bfs()
    print(f'Problem {tc}: {result}')
    
    tc += 1