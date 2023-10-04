def boj14938():
    import heapq
    n, m, r = map(int, input().split())
    t = list(map(int, input().split()))
    arr = [[] for _ in range(n+1)]
    for i in range(r):
        a, b, l = map(int, input().split())
        arr[a].append((b, l))
        arr[b].append((a, l))

    def dij(arr, start):
        distance = [int(1e9)] * (n + 1)
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
        return distance
    mx = 0
    for k in range(n + 1):
        ans = dij(arr, k)
        sv = 0
        for j in range(1, n + 1):
            if ans[j] <= m:
                sv += t[j-1]
        if mx < sv:
            mx = sv
    print(mx)


boj14938()
