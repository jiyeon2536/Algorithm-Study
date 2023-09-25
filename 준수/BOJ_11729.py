def hanoi(first, second, third, n):
    if n == 1:
        pass
    elif n == 2:
        # 탑 높이가 2일 경우 3가지 행동으로 정리 가능
        print(first, second)
        print(first, third)
        print(second, third)
    else:
        # 하노이의 탑의 규칙
        # 3가지 영역만을 이용하여 탑을 쌓아올리기 때문에 일정한 패턴이 존재
        hanoi(first, third, second, n - 1)
        print(first, third)
        hanoi(second, first, third, n - 1)

import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 20
dp[0] = 1

# 하노이의 탑 이동 횟수
for i in range(1, 20):
    dp[i] = dp[i - 1] * 2 + 1

# 탑 높이가 1일 경우
if T == 1:
    print(1)
    print(1, 3)
# 탑 높이가 2 이상일 경우
else:
    print(dp[T - 1])
    hanoi(1, 2, 3, T)