def boj1715():
    from heapq import heappush, heappop
    N = int(input())
    arr = []
    for i in range(N):
        heappush(arr, int(input()))
    sv = 0
    while len(arr) > 1:
        x = heappop(arr)
        y = heappop(arr)
        sv += x + y
        heappush(arr, (x+y))
    print(sv)
boj1715()
