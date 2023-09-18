T, W = map(int, input().split())
# 인덱스 0은 패팅 값이고 W에 맞춰서 +1
dp = [[0] * (W + 2) for _ in range(T + 1)]

for idx in range(T):
    location = int(input())

    # 움직인 횟수
    for move in range(1, W + 2):
        # 현 위치에서 자두를 먹을 수 있을까?
        if move % 2 == location % 2:
            # 자두를 먹었다면
            # 움직여서 먹을 수 있었던 경우와 움직이지 않았을 경우
            dp[idx + 1][move] = max(dp[idx][move - 1], dp[idx][move]) + 1
        else:
            # 못 먹었으면 그동안 먹었던 자두의 갯수만 기록
            dp[idx + 1][move] = dp[idx][move]
            
print(max(dp[T]))