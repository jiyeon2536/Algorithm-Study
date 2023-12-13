def bfs():
    visited = [1000 for _ in range(101)]
    queue = [1]
    visited[1] = 0

    while queue:
        v = queue.pop(0)

        if graph[v]:
            visited[graph[v][0]] = visited[v]
            v = graph[v][0]

        for move in range(1, 7):
            nv = v + move

            if nv >= 100:
                nv = 100

            if visited[nv] > visited[v] + 1: 
                queue.append(nv)
                visited[nv] = visited[v] + 1
        
    print(visited[100])



N, M = map(int, input().split())

graph = [[] for _ in range(101)]

for _ in range(N + M):
    s, e = map(int, input().split())

    graph[s].append(e)

bfs()