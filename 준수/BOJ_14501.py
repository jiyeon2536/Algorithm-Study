N = int(input())
dp = [0 for _ in range(N + 1)]
mx_val = 0

for idx in range(N):
    period, profit = map(int, input().split())

    # idx 날에 상담을 했을 때, 금액을 받는 날부터 경우의 수를 비교
    # 상담을 끝내고 바로 다른 상담을 했을 경우는 최적의 해가 아닐 수 있음
    for jdx in range(idx + period, N + 1):
        if dp[jdx] < dp[idx] + profit:
            dp[jdx] = dp[idx] + profit

print(max(dp))