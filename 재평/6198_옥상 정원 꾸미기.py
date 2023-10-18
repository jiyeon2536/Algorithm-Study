import sys
input = sys.stdin.readline

buildings = []
N = int(input())

for _ in range(N):
    buildings.append(int(input()))

stack = []
cnt = 0

for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    stack.append(building)
    cnt += len(stack) - 1

print(cnt)