import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [-1] * N
stack = []

for i in range(N):
    if stack:
        while True:
            if not stack or stack[-1][1] >= A[i]:
                break
            if stack[-1][1] < A[i]:
                idx, v = stack.pop()
                result[idx] = A[i]
    stack.append((i, A[i]))

print(*result)
