N = int(input())
M = int(input())

res_matrix = [[100001 * N] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    res_matrix[a][b] = min(c, res_matrix[a][b])

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                res_matrix[i][j] = 0
            else:
                res_matrix[i][j] = min(res_matrix[i][j], res_matrix[i][k] + res_matrix[k][j])

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if res_matrix[x][y] == 100001 * N:
            print(0, end=" ")
        else:
            print(res_matrix[x][y], end=" ")
    print()