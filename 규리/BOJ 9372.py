import sys
input = sys.stdin.readline

def dfs(v):
    global cnt
    if visited[v] == True:
        return
    visited[v] = True
    cnt += 1
    for u in graphs[v]:
        dfs(u)

T = int(input())
for _ in range(T):
    # 국가의 수 N, 비행기의 종류 M
    N, M = map(int, input().split())
    cnt = 0
    graphs = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        # a와 b를 왕복하는 비행기
        a, b = map(int, input().split())
        graphs[a].append(b)
        graphs[b].append(a)

    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i)

    print(cnt-1)
