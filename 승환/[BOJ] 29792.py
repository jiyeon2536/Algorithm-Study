def boj29792():
    import math
    N, M, K = map(int, input().split())
    dmg = []
    for i in range(N):
        D = int(input())
        dmg.append(D)
    cnt = []
    for i in range(K):
        P, Q = map(int, input().split())
        cnt.append((P, Q))

    res = []

    def subset(N, i, s, k):
        nonlocal mtx
        # 기저조건
        if i == N:
            tmp = 0
            for j in range(len(res)):
                tmp += math.ceil(res[j] / k)

            if tmp <= 900:
                if mtx < s:
                    mtx = s
            return

        # i 번째에 있는 요소를 사용o
        res.append(cnt[i][0])
        subset(N, i + 1, s + cnt[i][1], k)

        # i 번째에 있는 요소를 사용x
        res.pop()
        subset(N, i + 1, s, k)

    ans = []
    for r in range(N):  #
        k = dmg[r]
        mtx = 0
        subset(len(cnt), 0, 0, k)
        ans.append(mtx)
    answer = 0
    ans.sort(reverse=True)
    # print(ans)
    for i in range(M):
        answer += ans[i]
    print(answer)


boj29792()
