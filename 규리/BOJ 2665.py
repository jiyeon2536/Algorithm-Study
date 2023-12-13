import heapq

def bfs():
    q = [(0, 0, 0)]
    check = [[0] * N for _ in range(N)]  # 방문체크, 검->흰 바꾼 횟수 저장
    check[0][0] = 1

    while q:
        c, x, y = heapq.heappop(q)
        if x == y == N-1:
            print(c-1)
            break
        for dx, dy in [0, 1], [-1, 0], [0, -1], [1, 0]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 0:
                if arr[nx][ny] == 1:  # 흰 방
                    check[nx][ny] = check[x][y]
                    heapq.heappush(q, (check[nx][ny], nx, ny))
                else:  # 검은 방
                    check[nx][ny] = check[x][y] + 1
                    heapq.heappush(q, (check[nx][ny], nx, ny))


N = int(input())  # 한줄에 들어가는 방의 수
arr = [list(map(int, input())) for _ in range(N)]  # 0:검은방, 1:흰방
bfs()
