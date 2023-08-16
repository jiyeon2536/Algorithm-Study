def dfs(graph, start):
    visited = set()
    stack = [start]
    route = []

    while stack:
        vertex = stack.pop()

        for item in reversed(graph[vertex]):
            if item not in visited:
                stack.append(item)
        
        if vertex not in visited:
            visited.add(vertex)
            route.append(vertex)

    return route


computer_num = int(input())
pair_num = int(input())

network = dict()

for pairs in range(pair_num):
    n, m = map(int, input().split())

    network.setdefault(n, [])
    network.setdefault(m, [])
    network[n].append(m)
    network[m].append(n)

if computer_num == 1:
    print(0)
else:
    print(len(dfs(network, 1)) - 1)