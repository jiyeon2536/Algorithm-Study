def dfs(x, y, s):
    global mn

    # 다른 경로의 결과 값보다 현재 값이 크다면 재귀 중단
    if s > mn:
        return
    
    # 이차원 배열의 끝에 도착한 경우
    if x == N - 1 and y == N - 1 and mn > s:
        mn = s
        return

    for move in range(2):
        nx = x + dx[move]
        ny = y + dy[move]

        if nx < N and ny < N:
            # 재귀를 통해 경로의 합 계산
            dfs(nx, ny, s + arr[nx][ny])


# 오른쪽 또는 아래로 이동
dx = [1, 0]
dy = [0, 1]

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=" ")
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 내 생년월일
    mn = 980309

    dfs(0, 0, arr[0][0])
    print(mn)