V = int(input())  # 정점 개수
N = int(input())  # 간선 개수

# 정점 연결 정보
adj = []
for i in range(N):
    c1, c2 = map(int, input().split())
    adj.append(c1)
    adj.append(c2)

# 인접리스트
graphs = [[] for _ in range(V + 1)]
for idx in range(0, len(adj), 2):
    u = adj[idx]
    v = adj[idx + 1]
    graphs[u].append(v)
    graphs[v].append(u)

# 방문 체크
visited = [False for _ in range(V + 1)]

def dfs(v):
    global cnt, visited
    visited[v] = True
    for u in graphs[v]:
        if visited[u] == True:
            continue
        dfs(u)

dfs(1)
print(visited.count(True) - 1)
