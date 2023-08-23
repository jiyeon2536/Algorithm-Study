def dfs(x, y):
    global result, mn
    if mn < result:
        return
    if x == N-1 and y == N-1:
        mn = result
        return
    for dx, dy in [(0, 1), (1, 0)]:
        nx, ny = x+dx, y+dy
        if nx < N and ny < N:
            result += box[nx][ny]
            dfs(nx, ny)
            result -= box[nx][ny]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    result = box[0][0]
    mn = 10000
    dfs(0, 0)

    print(f'#{tc} {mn}')
