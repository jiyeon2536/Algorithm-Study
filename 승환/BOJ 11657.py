def boj11657():
    import heapq
    N, M = map(int, input().split())
    arr = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr.append((a, b, c))
    distance = [1e9] * (N + 1)
    # print(arr)

    def f(start):
        distance[start] = 0
        for k in range(N):
            for i, nxt, cst in arr:
                if distance[i] != 1e9 and distance[nxt] > distance[i] + cst:
                    distance[nxt] = distance[i] + cst
                    if k == N - 1:
                        return True
        return False

    ans = f(1)
    if ans:
        print('-1')
    else:
        for i in distance[2:]:
            if i == 1e9:
                print(-1)
            else:
                print(i)


boj11657()
