def dfs():
    visited = [False] * (N + 1)
    visited[1] = True
    # 루트가 1일 때 dfs 시작!
    stack = [1]

    while stack:
        # 부모 노드
        vertex = stack.pop()

        # 방문하지 않은 자식 노드의 부모는 vertex가 된다
        for nv in adj_list[vertex]:
            if visited[nv] == False:
                visited[nv] = True
                # 방문한 자식 노드부터 다시 탐색
                par_list[nv] = vertex
                stack.append(nv)


N = int(input())

adj_list = [[] for _ in range(N + 1)]
# 부모 노드의 번호를 저장
par_list = [0] * (N + 1)

# 양방향 간선으로 인접 리스트 만들기
for _ in range(N - 1):
    v1, v2 = map(int, input().split())

    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

dfs()
# 2번 노드부터 부모 노드의 번호를 출력
print(*par_list[2:], sep="\n")
