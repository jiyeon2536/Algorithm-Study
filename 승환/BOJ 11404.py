def boj11404():
    import heapq
    N = int(input())
    m = int(input())
    arr = [[] for _ in range(N+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
    # n개의 줄을 출력해야 한다. --> 출발점을 여러 개로 해서 다익스트라 돌려라

    def dij(arr, start):
        distance = [int(1e9)] * (N + 1)
        distance[start] = 0
        min_heap = [(0, start)]

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if cost > distance[node]:
                continue

            for nxt, w in arr[node]:
                n_cost = cost + w
                if distance[nxt] > n_cost:
                    distance[nxt] = n_cost
                    heapq.heappush(min_heap, (n_cost, nxt))
        return distance[1:]
    for i in range(1, N+1):
        ans = dij(arr, i)
        for j in range(len(ans)):
            if ans[j] == 1e9:
                print(0, end=' ')
            else:
                print(ans[j], end=' ')
        print()


boj11404()
