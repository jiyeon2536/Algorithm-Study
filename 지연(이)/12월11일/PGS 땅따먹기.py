def solution(land):
    answer = 0
    dp = [[0]*4 for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(4):
            if i==0:
                dp[i][j] = land[i][j]
            else:
                mx = 0
                for k in range(4):
                    if k!=j:
                        mx = max(mx, dp[i-1][k])
                dp[i][j] = land[i][j]+mx
    return max(dp[len(land)-1][:])

