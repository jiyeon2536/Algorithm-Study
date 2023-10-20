def boj2252():
    from collections import deque
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    
    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
    # 모든 정점의 in_degree를 설정한다
    # 그래프에서 자신을 가리키는 방향
    in_degree = [0] * (N + 1)
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            in_degree[arr[i][j]] += 1

    q = deque()
    visited = [0] * (N + 1)
    # in_degree가 0인 정점을 q에 삽입하고 방문 표시한다.
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)
            visited[i] = 1
    while q:
        x = q.popleft()
        # q를 돌면서 나오는게 순서
        print(x, end=' ')
        for i in range(len(arr[x])):
            # 가리키는 방향으로 돌면서 인접 정점을 찍었으니 하나씩 줄인다.
            in_degree[arr[x][i]] -= 1
            # 만약 0이면 q에 추가한다
            if in_degree[arr[x][i]] == 0:
                q.append(arr[x][i])


boj2252()
