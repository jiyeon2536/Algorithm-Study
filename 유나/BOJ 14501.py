import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]

dp = [0] * (n+1)

# i번째 까지 일했을 때 최대 수익읠 계산히고자
for i in range(n):
    # i 인덱스의 상단 기간 이후 일자의 dp에 벌 수 있는 금액 입력
    for j in range(i+arr[i][0], n+1):
        # 만약에 이전에 입력되어 있던 값이 이번 인덱스에서 번 돈 보다 작다면 갱신
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

# 가장 마지막 일자의 금액 출력
print(dp[-1])
