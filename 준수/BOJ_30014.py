from collections import deque

N = int(input())
P = sorted(list(map(int, input().split())))

necklace = deque()

while P:
    Ai = P.pop()

    if not necklace:
        necklace.append(Ai)
        continue

    if necklace[0] >= necklace[-1]:
        necklace.appendleft(Ai)
    else:
        necklace.append(Ai)

answer = 0

for i in range(N):
    answer += necklace[i - 1] * necklace[i]

print(answer)
print(*necklace)
