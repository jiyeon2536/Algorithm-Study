dx = [1, 0, -1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

N, M = map(int, input().split())
matrix = []
shark = []
mx_safe = 0

# 순회를 돌면서 상어가 있는 좌표는 shark 배열에 담고
# matrix 이차원 배열을 완성
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            shark.append((i, j))
    matrix.append(line)

# bfs 순회
while shark:
    x, y = shark.pop(0)

    # 8방향 탐색
    for move in range(8):
        nx = x + dx[move]
        ny = y + dy[move]

        # 안전거리가 측정되지 않은 곳의 안전거리를 측정함
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y] + 1
            shark.append((nx, ny))

            # 두 번 이상 사용할 값을 따로 변수에 지정
            next_safe = matrix[nx][ny]

            # 안전거리 최댓값 갱신
            if next_safe > mx_safe:
                mx_safe = next_safe

# 시작점이 1이었으니 1을 빼줌
print(mx_safe - 1)