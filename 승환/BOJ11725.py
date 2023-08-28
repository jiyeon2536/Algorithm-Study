def bfs(r):
    q = [r]
    while q:
        r = q.pop(0)
        for k in arr[r]:
            if visited[k] == 0:
                q.append(k)
                visited[k] = r
N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [0] * (N+1)
visited[1] = 1
bfs(1)
for i in range(2, len(visited)):
    print(visited[i])
