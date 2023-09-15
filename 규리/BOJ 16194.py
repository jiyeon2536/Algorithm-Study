#  구매하려고 하는 카드 개수
N = int(input())
P = [0] + list(map(int, input().split()))
DP = [0]*(N+1)

for i in range(1, N+1):
    DP[i] = DP[i-1] + P[1]
    for j in range(2, i+1):
        DP[i] = min(DP[i-j]+P[j], DP[i])

print(DP[N])
