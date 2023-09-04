N = int(input())
ieq = input().split()

mx_dp = [num for num in range(9, 8 - N, -1)]
mn_dp = [num for num in range(N + 1)]

for i in range(N + 1):
    for j in range(N):
        if ieq[j] == '<':
            if mx_dp[j] > mx_dp[j + 1]:
                mx_dp[j], mx_dp[j + 1] = mx_dp[j + 1], mx_dp[j]

            if mn_dp[j] > mn_dp[j + 1]:
                mn_dp[j], mn_dp[j + 1] = mn_dp[j + 1], mn_dp[j]

        if ieq[j] == '>':
            if mx_dp[j] < mx_dp[j + 1]:
                mx_dp[j], mx_dp[j + 1] = mx_dp[j + 1], mx_dp[j]

            if mn_dp[j] < mn_dp[j + 1]:
                mn_dp[j], mn_dp[j + 1] = mn_dp[j + 1], mn_dp[j]

print(*mx_dp, sep='')
print(*mn_dp, sep='')