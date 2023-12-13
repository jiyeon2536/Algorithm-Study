import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

result = [[] for _ in range(N)]
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()].append(A[i])
    stack.append(i)

for i in range(N):
    if result[i]:
        print(result[i].pop(), end=' ')
    else:
        print(-1, end=' ')
