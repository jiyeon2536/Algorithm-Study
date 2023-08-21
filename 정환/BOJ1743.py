def bfs(s):
    global mx

    if arr[s[0]][s[1]] == 1:
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
        queue = []
        queue.append(s)

        cnt = 1

        while queue:
            n = queue.pop(0)
            for k in range(4):
                ni, nj = n[0] + di[k], n[1] + dj[k]
                if 0 <= ni < N and 0 <= nj <M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    cnt += 1
                    queue.append((ni, nj))
        # 최댓값 갱신
        if cnt > mx:
            mx = cnt

# N : 통로의 세로길이, M : 통로의 가로길이 , K : 음식물 쓰레기의 개수
N, M, K = map(int, input().split())

# 음식물이 떨어진 좌표 리스트
trashs = [list(map(int, input().split())) for _ in range(K)]

# BFS 를 위한 방문표시 리스트
visited = [[0] * M for _ in range(N)]
# 음식물이 떨어진 위치를 담은 좌표리스트를 2차원 리스트로 표현
arr = [[0] * M for _ in range(N)]
for trash in range(len(trashs)):
    arr[trashs[trash][0] - 1][trashs[trash][1] - 1] = 1

# 음식물 크기의 최댓값을 저장하기 위해 기준을 0으로 설정
mx = 0

# 음식물이 위치한 좌표를 순회하면서
for i in range(N):
    for j in range(M):
        # 음식물이 존재하고, 아직 방문하지 않았다면
        if arr[i][j] == 1 and visited[i][j] == 0:
            # 현재 좌표를 저장하고
            s = (i, j)
            # 방문 표시를 한 후,
            visited[s[0]][s[1]] = 1
            # 현재 좌표의 bfs 실행
            bfs(s)

print(mx)
