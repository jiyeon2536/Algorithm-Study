import sys
input = sys.stdin.readline

N = int(input())

arr = [0] + list(map(int, input().split()))
# N 을 만들 수 있는 경우에서 가장 최솟값만 담을 리스트
dp = [0] * (N + 1)

# 순서대로 1, 2, 3 ...
for i in range(1, N + 1):
    # 일단 1장의 카드만 샀을 때의 비용을 저장
    dp[i] = arr[i]
    # 1장으로만 이루기 전까지의 개수와 비용을 순회하면서
    for j in range(1, i):
        # 가장 비용이 적게 드는 상황을 dp에 저장한다면 이후로 따로 계산 필요 x
        tmp = dp[j] + arr[i - j]
        # 이전 까지 구한 dp[i] 는 비용이 최소인 경우이므로
        # 그 값보다 작은 비용이라면 최소값을 다시 dp[i]에 갱신
        if tmp < dp[i]:
            dp[i] = tmp


print(dp[N])