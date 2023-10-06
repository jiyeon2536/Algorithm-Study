def compare(lst, lst2):
    res_sum = 0
    res2_sum = 0

    for node in lst:
        res_sum += people_num[node]

    for node2 in lst2:
        res2_sum += people_num[node2]

    return abs(res_sum - res2_sum)


def check_adj(arr):
    visit = [False] * (N + 1)
    start = arr[0]
    visit[start] = True
    queue = [start]
    route = [start]

    while queue:
        vertex = queue.pop(0)

        for node in adj_list[vertex]:
            if node in arr and visit[node] == False:
                visit[node] = True
                queue.append(node)
                route.append(node)

    if len(arr) == len(route):
        return True
    else:
        return False


def comb(area_num, res, mx, visit):
    global mn

    new_visit = visit[:]

    if area_num == mx:
        res2 = [x for x in range(1, N + 1) if x not in res]

        if check_adj(res[:]) and check_adj(res2[:]):
            res_diff = compare(res, res2)

            if mn > res_diff or mn < 0:
                mn = res_diff

    for node in range(1, N + 1):
        if new_visit[node] == False:
            new_visit[node] = True
            comb(area_num + 1, res + [node], mx, new_visit)


N = int(input())
people_num = [0] + list(map(int, input().split()))
adj_list = [[] for _ in range(N + 1)]

for idx in range(1, N + 1):
    num, *adj = map(int, input().split())

    adj_list[idx].extend(adj)

visited = [False for _ in range(N + 1)]
mn = -1

for num in range(1, N // 2 + 1):
    comb(0, [], num, visited)

print(mn)