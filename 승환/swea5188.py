dx = [0, 1]
dy = [1, 0]
def dfs(s, g, sv):
    global mi
    if sv > mi:  # 기저 조건
        return
    x = s[0]
    y = s[1]
    if x == g[0] and y == g[1]:
        if sv < mi:
            mi = sv
        return
    for k in range(2):  # 델타 검색
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            #sv += arr[nx][ny]  여기가 문제?  재귀 돌리는데 더해진 값이 남아있는다.
            s = (nx, ny)  # 시작점 갱신
            dfs(s, g, sv+arr[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    g = (N-1, N-1)  # 도착 지점
    mi = 9999999
    s = (0, 0)  # 출발지
    dfs(s, g, arr[0][0])  # dfs
    print(f'#{tc} {mi}')
