N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N - 1):
    v, u = map(int, input().split())

    graph[v].append(u)
    graph[u].append(v)

D_count = 0
G_count = 0

for i in range(1, N + 1):
    temp = len(graph[i])

    if (temp - 2) > 0:
        G_count += temp * (temp - 1) * (temp - 2) // 6

    visited[i] = True
    for j in graph[i]:
        if visited[j] == False:
            temp1 = len(graph[i]) - 1
            temp2 = len(graph[j]) - 1
    
            if temp1 >= 1 and temp2 >= 1:
                D_count += temp1 * temp2

if D_count == G_count * 3:
    print('DUDUDUNGA')
elif D_count > G_count * 3:
    print('D')
else:
    print('G')