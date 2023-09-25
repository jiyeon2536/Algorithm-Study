def baek1647():
    # 크루스칼 사용한다.(간선이 많기 때문)
    N, M = map(int, input().split())
    graph = []
    for i in range(M):
        a, b, c = map(int, input().split())
        graph.append([a, b, c])
    graph.sort(key= lambda k: k[2])
    parents = [i for i in range(N+1)]

    def find(x):
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]

    def union(a, b):
        na = find(a)
        nb = find(b)

        if na > nb:
            parents[na] = nb
        else:
            parents[nb] = na

    cnt = 0
    sv = 0
    mx_w = 0
    for f, t, w in graph:
        if find(f) != find(t):
            cnt += 1
            if w > mx_w:
                mx_w = w
            sv += w
            union(f, t)
            if cnt == M:
                break
    print(sv - mx_w)
baek1647()
