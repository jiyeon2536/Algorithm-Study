def bfs(sx, sy):
    global visited, cnt
    que = []
    que.append([sx,sy])
    visited[sx][sy] = 1
    while que:
        i, j = que.pop(0)
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                que.append([ni, nj])
                visited[ni][nj] = 1

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split()) # 배추밭 가로 / 세로/ 배추 심은 위치 개수
    arr = [[0] * m for _ in range(n)]

    # k번 순회하면서 배추 위치 표기
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    visited = [[0] * m for _ in range(n)]
    # 모든 인덱스를 순회
    for r_idx in range(n):
        for c_idx in range(m):
            # 배추가 있고, 방문한 적 없는 곳에 대하여 bfs 진행
            if arr[r_idx][c_idx] == 1 and visited[r_idx][c_idx] == 0:
                bfs(r_idx, c_idx)
                cnt += 1 # 필요한 지렁이 더해주기


    print(cnt)
