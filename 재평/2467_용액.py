import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))

l = 0
r = N - 1

cc = float('inf')
a = 0
b = 0

while l < r:
    nxt = solution[l] + solution[r]
    if abs(nxt) <= cc:
        a = l
        b = r
        cc = abs(nxt)
    if nxt <= 0:
        l += 1
    else:
        r -= 1

print(solution[a], solution[b])