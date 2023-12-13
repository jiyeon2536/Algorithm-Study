def bfs(start, matrix):
    # 바이러스의 위치를 담은 배열로 bfs 시작
    queue = start

    while queue:
        x, y = queue.pop(0)

        for move in range(4):
            nx = x + dx[move]
            ny = y + dy[move]
            
            # 4방향 탐색하며 벽으로 막혀있지 않으면 바이러스 증식
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                queue.append([nx, ny])

    safety_area = 0

    # 안전 영역 크기 계산
    for h in range(N):
        for w in range(M):
            if matrix[h][w] == 0:
                safety_area += 1

    return safety_area


def dfs(wall_num, matrix):
    global mx_safe

    # 각 좌표에 벽을 세운 경우를 따로 담을 2차원 배열
    copy_matrix = []

    # 2차원 배열 deep copy
    for line in matrix:
        copy_matrix.append(line[:])

    # 벽을 3개 세우면 bfs 시작
    if wall_num == 3:
        a = bfs(virus[:], copy_matrix)

        # 안전 영역의 최대 크기 갱신
        if mx_safe < a:
            mx_safe = a
        
        return
    
    # matrix 좌표가 1인 경우 벽을 세우거나 세우지 않음
    for i in range(N):
        for j in range(M):
            if copy_matrix[i][j] == 0:
                copy_matrix[i][j] = 1
                dfs(wall_num + 1, copy_matrix)
                copy_matrix[i][j] = 0


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
lab = []
virus = []
mx_safe = 0

# 순회를 돌면 바이러스가 있는 좌표를 virus 배열에 담음
# lab 이차원 배열을 설정
for n in range(N):
    line = list(map(int, input().split()))

    for m in range(M):
        if line[m] == 2:
            virus.append([n, m])

    lab.append(line)

# 일단 dfs로 벽을 3개 세운다. 
dfs(0, lab)
print(mx_safe)