def bfs(x):
    global visited
    # (회원번호, 가까운정도(거리))
    q = [(x, 0)]
    # graph[x]에 있는 회원은 친구 사이
    for a in graph[x]:
        q.append((a, 1))
    visited[x] = True
    
    # 가장 거리가 먼 회원 갱신(mx)
    mx = 0
    while q:
        v, cnt = q.pop(0)
        for u in graph[v]:
            if visited[u] == False:
                mx = max(mx, cnt+1)
                q.append((u, cnt+1))  # 다른 회원을 거쳐서 아는 사이 -> +1
                visited[u] = True

    return mx

N = int(input())  # 회원 수
graph = [[] for _ in range(N+1)]
while True:
    A, B = map(int, input().split())
    if A == B == -1:
        break
    graph[A].append(B)
    graph[B].append(A)

mn = 10 ** 6
result = [mn]

for i in range(1, N+1):
    visited = [False] * (N+1)
    ans = bfs(i)
    mn = min(mn, ans)  # 가장 점수가 적은 사람이 회장
    result.append(ans)

res = [mn, result.count(mn)]
for i in range(1, N+1):
    if result[i] == mn:
        res.append(i)

print(*res[:2])
print(*res[2:])
