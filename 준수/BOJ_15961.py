import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
arr = [0] * N
dp = [0] * (D + 1)

for idx in range(N):
    sushi = int(input())
    arr[idx] = sushi

answer = 1
dp[C] += 1

for i in range(K):
    if dp[arr[i]] == 0:
        answer += 1
    dp[arr[i]] += 1

temp = answer

for i in range(1, N):
    dp[arr[i - 1]] -= 1

    if dp[arr[i - 1]] == 0:
        temp -= 1

    if dp[C] == 0:
        temp += 1
        dp[C] += 1

    if dp[arr[(i + K - 1) % N]] == 0:
        temp += 1

    dp[arr[(i + K - 1) % N]] += 1

    answer = max(answer, temp)

print(answer)
