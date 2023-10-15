import sys
from collections import  deque
input = sys.stdin.readline

# 진행 순서
# 1. arr 순회하면서 bfs를 통해 존재하는 각 섬들을 구분 (한 섬씩 만날 때마다 cnt += 1 로 구분)
# 2. 섬이 구분되면 각 섬에서 다른 섬으로 가는 다리를 놓음 (크기는 최소 2 이상, 다리 위로 다리 생성 가능)
# 3. 각 섬에서 놓을 수 있는 리스트를 구성하였으면 kruskal 을 이용하여 모든 섬의 최소 스패닝 트리 구성

def find_set(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find_set(parents[x])
        return parents[x]


def union(x, y):
    px, py = find_set(x), find_set(y)

    if px != py:
        if px < py:
            parents[px] = py
        else:
            parents[py] = px


def bfs(s):
    global cnt

    queue = deque()
    queue.append(s)
    visited[s[0]][s[1]] = cnt

    while queue:
        n = queue.popleft()

        for k in range(4):
            ni, nj = n[0] + di[k], n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                queue.append([ni, nj])
                visited[ni][nj] = cnt
    cnt += 1

    return visited


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

cnt = 1
parents = [_ for _ in range(7)]

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j]:
            bfs([i, j])

graph = [[] for _ in range(7)]

tmp = []
mx = 2
for x in range(N):
    for y in range(M):
        if visited[x][y] != 0:
            if visited[x][y] > mx:
                mx = visited[x][y]
            for w in range(4):
                nx, ny = x + di[w], y + dj[w]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                    inner_cnt = 1
                    while 0 <= nx + di[w] < N and 0 <=  ny + dj[w] < M and visited[nx][ny] == 0:
                        nx, ny = nx + di[w], ny + dj[w]
                        if inner_cnt >= 2 and visited[nx][ny] != 0:
                            if [visited[x][y], visited[nx][ny], inner_cnt] not in tmp and [visited[nx][ny], visited[x][y], inner_cnt] not in tmp:
                                tmp.append([visited[x][y], visited[nx][ny], inner_cnt])
                                break
                        inner_cnt += 1

tmp.sort(key=lambda x:x[2])


# 맵 상에 존재하는 섬들을 최소 스패닝 트리로 구성
island_cnt = 1
cost = 0

for kru in range(len(tmp)):
    if island_cnt == mx:
        break
    if find_set(tmp[kru][0]) != find_set(tmp[kru][1]):
        island_cnt += 1
        cost += tmp[kru][2]
        union(tmp[kru][0], tmp[kru][1])

# 모든 섬이 최소 스패닝 트리를 이루고 있는지 체크
check = True
for chk1 in range(1, mx + 1):
    if check == False:
        break
    for chk2 in range(chk1 + 1, mx + 1):
        if find_set(chk1) != find_set(chk2):
            check = False
            break


if cost == 0 or not check:
    print(-1)
else:
    print(cost)
