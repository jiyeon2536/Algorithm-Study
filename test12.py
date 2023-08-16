def dfs(n):
    global visited
    visited[n] = 1
    for i in arr[n]:
        if visited[i] == 1:
            continue
        dfs(i)


n = int(input())
m = int(input())

visited = [0] * (n+1)
arr = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
dfs(1)
cnt = 0
for i in range(len(visited)):
    if visited[i] == 1:
       cnt += 1
print(cnt-1)