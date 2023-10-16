def boj6198():
    import sys
    input = sys.stdin.readline

    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    cnt = 0
    stk = []
    for i in arr:
        while stk and stk[-1] <= i:
            stk.pop()
        stk.append(i)

        cnt += len(stk) - 1
    print(cnt)
        # for j in range(i+1, N, 1):
        #     if stk[i] <= stk[j]:
        #         break
        #     else:
        #         cnt += 1
        # 위 코드는 시간초과 발생함


boj6198()
