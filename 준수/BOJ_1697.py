def bfs(start, end):
    queue = [start]
    num = 0
    # 각 위치에 도착한 시간을 기록하는 배열
    dp = [0] * 100001

    while queue:
        # 동생을 찾는 시간
        num += 1

        # 1초마다 이동할 수 있는 경우를 모두 탐색한다는 의미의 반복문
        for _ in range(len(queue)):
            tmp = queue.pop(0)
            tmp_list = [tmp + 1, tmp - 1, tmp * 2]

            for i in tmp_list:
                if 0 <= i < 100001:
                    if dp[i] == 0:
                        # 도착한 위치에 소요된 시간을 기록
                        dp[i] = num
                        queue.append(i)

        # 만약 동생을 찾았다면 bfs 중단
        if dp[end]:
            return dp[K]


N, K = map(int, input().split())

# 수빈이와 동생의 위치가 같으면 0
if N == K:
    print(0)
else:
    print(bfs(N, K))
