# 앱의 수, 메모리의 양
n, m = map(int, input().strip().split())
app = [0] + list(map(int, input().strip().split()))
cost = [0] + list(map(int, input().strip().split()))

# 행 : 앱의 개수 / 열 : 최대 비용
total = sum(cost)
dp = [[0] * (total + 1) for _ in range(n+1)]
res = total
for i in range(n+1):
    for j in range(total + 1):
        if 0 <= j - cost[i] <= total:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - cost[i]] + app[i])
        else:
            dp[i][j] = dp[i - 1][j]

        if dp[i][j] >= m:
            res = min(res, j)
print(res)
