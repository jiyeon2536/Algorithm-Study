def dfs(graph, start):
    # 방문한 노드의 번호를 담는 세트
    visited = set()
    stack = [start]
    # 1번과 이어진 컴퓨터의 목록을 담는 리스트
    route = []

    while stack:
        vertex = stack.pop()

        # vertex 정점에 이어진 정점들 중 visited에 없는 정점을 stack에 추가
        for item in reversed(graph[vertex]):
            if item not in visited:
                stack.append(item)

        # vertex가 visited에 없을 경우 visited와 route에 vertex 추가        
        if vertex not in visited:
            visited.add(vertex)
            route.append(vertex)

    return route


computer_num = int(input())
pair_num = int(input())

# 각 정점에 이어진 정점들의 정보를 담는 딕셔너리
network = dict()

for pairs in range(pair_num):
    n, m = map(int, input().split())

    # 각 정점을 key로 설정하고 value는 빈 리스트로 초기화
    network.setdefault(n, [])
    network.setdefault(m, [])

    # 무방향 그래프
    # 정점에 이어진 모든 정점 정보를 딕셔너리 value에 추가
    network[n].append(m)
    network[m].append(n)

# 주어진 컴퓨터의 수가 1일 경우... 0 출력
if computer_num == 1:
    print(0)
# 1번을 제외한 1번과 이어진 컴퓨터의 수 출력
else:
    print(len(dfs(network, 1)) - 1)