import sys
input = sys.stdin.readline

import heapq

N = int(input())
heap = []

for _ in range(N):
    tmp = int(input())
    heapq.heappush(heap, tmp)

compare = 0
score = 0

while len(heap) > 1:
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)
    compare = A + B
    score += compare
    heapq.heappush(heap, compare)

print(score)