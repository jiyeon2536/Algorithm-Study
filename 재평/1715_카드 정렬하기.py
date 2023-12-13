import sys
input = sys.stdin.readline
import heapq

N = int(input())
card_deck = []
for _ in range(N):
    heapq.heappush(card_deck, int(input()))
cnt = 0
for _ in range(N-1):
    a = heapq.heappop(card_deck)
    b = heapq.heappop(card_deck)
    cnt += (a+b)
    heapq.heappush(card_deck, a+b)
print(cnt)