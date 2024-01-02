# 땅 따먹기
def solution(land):
    answer = 0
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    for i in range(n):
        for j in range(4):
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                for k in range(4):
                    if k == j:
                        continue
                    else:
                        dp[i][j] = max(dp[i][j], dp[i-1][k] + land[i][j])

    answer = max(dp[-1])
    return answer