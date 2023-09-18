import heapq

N, M = map(int, input().split())
cards = list(map(int, input().split()))
heap = []

# 최소 힙을 통해 작은 수가 먼저 pop 될 수 있게 만듦
for card in cards:
    heapq.heappush(heap, card)

for _ in range(M):
    # 가장 작은 수 2개를 뽑아서 
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)

    # 더한 뒤
    z = x + y

    # 힙 자료구조에 넣는다
    heapq.heappush(heap, z)
    heapq.heappush(heap, z)

print(sum(heap))