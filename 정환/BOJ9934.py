import sys
input = sys.stdin.readline

K = int(input())

arr = list(map(int, input().split()))

stairs = [[] for _ in range(K)]


# 그리디에 절여져서 중위순회를 까먹었어요 봐도 모르겠어요 알려주세요
for j in range(K):
    for i in range((2 ** (K - j) - 1) // 2, len(arr), 2 ** (K - j)):
        stairs[j].append(arr[i])

for k in stairs:
    print(*k)