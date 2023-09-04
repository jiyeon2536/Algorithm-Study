N, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
b_ = [list(map(int, input().split())) for _ in range(M)]
B = []
for i in zip(*b_):
    B.append(list(i))

for a in A:
    result = []
    for b in B:
        x = 0
        for i in range(M):
            x += a[i]*b[i]
        result.append(x)

    print(*result)
