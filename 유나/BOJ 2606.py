N = int(input()) # 컴퓨터 수
V = int(input()) # 간선의 수

visited = [0] * (N + 1) # 방문 체크
graphs = [[] for _ in range(N + 1)] # 지도

for _ in range(V):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)

def dfs(v): # dfs 변수 생성
    global visited
    visited[v] = 1
    for u in graphs[v]:
        if visited[u]: # 방문한 적 있으면 지나가라!
            continue
        dfs(u) # 아니면 돌아보기
dfs(1)
ans = sum(visited) - 1 # 감염시킨 컴퓨터 중 자기 자신 제외

print(ans)
 
