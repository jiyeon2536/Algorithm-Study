T = int(input())

def find(i, j):
    global mn
    global inner_sum

    di, dj = [0, 1], [1, 0]
    if i == N - 1 and j == N - 1:
        if mn > inner_sum:
            mn = inner_sum

    for k in range(2):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            inner_sum += arr[ni][nj]

            find(ni, nj)

            visited[ni][nj] = 0
            inner_sum -= arr[ni][nj]
            if inner_sum > mn:
                return


for tc in range(1, T + 1):
    N = int(input())
    i, j = 0, 0
    mn = 10000000000000
    arr = [list(map(int, input().split())) for _ in range(N)]
    inner_sum = arr[i][j]
    visited = [[0] * N for _ in range(N)]

    find(i, j)
    print(f'#{tc} {mn}')