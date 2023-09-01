def meetingroom3():
    N = int(input())
    # 시간대 다 집어넣고, 최대 개수 출력
    res = []
    for _ in range(N):
        [si, ei] = list(map(int, input().split()))
        res.append([si, ei])
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1])
    cnt = 1
    time = res[0][1]
    for j in range(1, N): #i
        if time <= res[j][0]:
            time = res[j][1]
            cnt += 1
    print(cnt)
