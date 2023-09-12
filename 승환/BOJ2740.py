N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))  # N * M 배열
M, k = map(int, input().split())
arr2 = []
for j in range(M):
    arr2.append(list(map(int, input().split())))  # M * k 배열
res = [[0] * k for _ in range(N)]  # 곱하면 N * k 형태 가로길이 k, 세로길이 N
for i in range(N):
    for r in range(M):
        for j in range(k):
            res[i][j] += arr[i][r] * arr2[r][j]  # 곱해서 넣어라.
for o in range(N):
    print(*res[o])
