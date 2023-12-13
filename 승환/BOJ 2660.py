def boj2660():
    from collections import deque
    def bfs(start):
        visited = [0] * (N + 1)
        q = deque()
        q.append(start)
        visited[start] = 1
        while q:
            x = q.popleft()
            for i in graph[x]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[x] + 1
        return visited

    N = int(input())
    graph = [[] for _ in range(N+1)]
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        graph[a].append(b)
        graph[b].append(a)
    # bfs로 visited 초기화 하면 된다.
    scr = 1e9  # 점수
    cnt = 0  # 후보의 수
    mem = []
    for i in range(1, N+1):
        ans = bfs(i)
        mx = -1
        for j in range(len(ans)):
            if mx < ans[j]:
                mx = ans[j]
        if mx < scr:
            cnt = 1
            scr = mx
            mem = [i]
        elif mx == scr:
            cnt += 1
            mem.append(i)
    print(scr-1, cnt)
    print(*mem)
    # 회장 후보의 점수와 후보의 수를 출력하고,
    # 두번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.
