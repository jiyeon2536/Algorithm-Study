import heapq

N = int(input())
cards = []
for _ in range(N):
    C = int(input())
    heapq.heappush(cards, C)  # 작은 수 앞으로

result = 0
while len(cards) > 1:  # 1장 남으면 멈춤
    # 가장 작은 두 값
    C1, C2 = heapq.heappop(cards), heapq.heappop(cards)
    v = C1 + C2
    result += v
    heapq.heappush(cards, v)  # 다시 cards에 넣음

print(result)
