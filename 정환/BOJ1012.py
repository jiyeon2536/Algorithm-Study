T = int(input())

def BFS():
    global cnt

    queue = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                queue.append((i, j))
                while queue:

                    for k in range(4):
                        ni, nj = i + di[k], j + dj[k]
                        if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 1 and visited[ni][nj] == False:
                            visited[ni][nj] = True
                            queue.append((ni, nj))
                    else:
                        queue.pop(0)

                    if queue:
                        i, j = queue[0]
                    else:
                        cnt += 1
    return cnt



for tc in range(T):
    # M : 배추밭의 가로길이
    # N : 배추밭의 세로길이
    # K : 배추의 위치의 개수
    M, N, K = map(int, input().split())

    # 배추밭에 심어져있는 배추를 표현할 2차원 리스트
    field = [[0] * M for _ in range(N)]
    # 각 좌표의 방문 현황
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        # X, Y : 배추의 위치 ( 이차원 리스트 좌표 형식 )
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    # BFS 용 사방탐색
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

    cnt = 0

    print(BFS())
