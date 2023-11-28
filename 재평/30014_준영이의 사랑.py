import sys
input = sys.stdin.readline
from collections import deque

# N개의 진주로 만들어진 목걸이 (원형)
N = int(input())
# 진주알의 가치
P = list(map(int, input().split()))
P.sort()
# 인접한 두 진주알 가치의 곱의 합이 최댓값이 되도록 ...
# 시간은 충분 ?
# 배열의 순서가 중앙값이 점점 크게 되도록 정렬...
# index = ['l', 'r']
# result = deque()
# for i in range(N):
#     num = P.pop()
#     position = i % 2
#     if index[position] == 'r':
#         result.appendleft(num)
#     else:
#         result.append(num)

result = deque()
for i in range(N):
    num = P.pop()
    position = i % 2
    if i % 2:
        result.appendleft(num)
    else:
        result.append(num)

total = 0
l = result[-1]
for i in range(N):
    r = result[i]
    total += l * r
    l = r

print(total)
print(*result)
