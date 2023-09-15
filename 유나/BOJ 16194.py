import sys
input = sys.stdin.readline


n = int(input().strip())
arr = [0] + list(map(int, input().strip().split()))

# 시작을 0으로 잡고, 나머지는 가능한 가장 큰 수로 지정
dp = [0] + [10 ** 7] * (n)

# dp[i] = 카드 i개 구매하는 최소 가격
# arr[j]= j개가 들어있는 카드팩 가격 이라고 했을때
# dp[i] = arr[j] + dp[i-j]
'''
dp[1] = min(dp[1], arr[1] + dp[0]
dp[2] = min(dp[2], arr[1] + dp[1]
        min(dp[2], arr[2] + dp[0]
dp[3] = min(dp[3], arr[1] + dp[2]
        min(dp[3], arr[2] + dp[1]
        min(dp[3], arr[3] + dp[0]
'''

# 순회하면서 최솟값 구하기
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], arr[j] + dp[i-j])

print(dp[n])
