def boj17471():
    import sys
    from collections import deque
    input = sys.stdin.readline

    def bfs(g):
        q = deque()
        chk = [False for _ in range(n)]
        q.append(g[0])
        chk[g[0]] = True
        cnt, answer = 1, 0
        while q:
            temp = q.popleft()
            answer += arr[temp]
            # 지나치는 값 추가.
            for i in graph[temp]:
                # g배열 안에 있고 방문한 적이 없다면 계속 진행 가능
                if i in g and not chk[i]:
                    chk[i] = True
                    cnt += 1
                    q.append(i)

        if cnt == len(g):
            return answer
        else:
            return False

    def dfs(cnt, x, end):
        nonlocal mn

        # 원하는 구역의 개수 만큼 도달 했을 때
        if cnt == end:
            g1, g2 = deque(), deque()

            # 방문 했으면 g1 그룹으로 방문하지 않았으면 g2그룹으로 넣어준다
            for i in range(n):
                if visited[i]:
                    g1.append(i)
                else:
                    g2.append(i)

            ans1 = bfs(g1)
            if not ans1:
                return
            ans2 = bfs(g2)
            if not ans2:
                return
            mn = min(mn, abs(ans1-ans2))
            return

        for i in range(x, n):
            if visited[i]:
                continue
            visited[i] = True
            dfs(cnt+1, i, end)
            visited[i] = False

    n = int(input())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(n)]
    for i in range(n):
        x = list(map(int, input().split()))
        for j in x[1:]:
            graph[i].append(j-1)

    mn = 1e9
    # 선거구가 2개로 나누어지기 때문에 n//2까지만 확인하면 된다.
    for i in range(1, n//2 + 1):
        visited = [False for _ in range(n)]
        # 구역 찾기
        dfs(0, 0, i)

    if mn == 1e9:
        print(-1)
    else:
        print(mn)


boj17471()
