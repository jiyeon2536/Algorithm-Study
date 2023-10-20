from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [[] for _ in range(N+1)]
arr = [0]*(N+1)
result = []

for _ in range(M):
    a, b = map(int, input().split())
    nums[a].append(b)
    arr[b] += 1

q = deque()
for i in range(1, N+1):
    if arr[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    result.append(x)
    for i in nums[x]:
        arr[i] -= 1
        if arr[i] == 0:
            q.append(i)

print(*result)
