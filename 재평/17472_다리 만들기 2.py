import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 셀 좌표를 땅 번호에 딕셔너리 형태로 mapping
land_dict = {}
# 각 셀의 땅 정보
land_list = []

# 땅의 개수 초기화
land_num = 0

# BFS로 맵 탐색
for i in range(N):
    for j in range(M):
        if map_arr[i][j] == 1 and not visited[i][j]:
            # 새로운 땅에 대한 큐 초기화
            queue = deque([(i, j)])
            visited[i][j] = True
            land_dict[(i, j)] = land_num
            land_list.append((i, j, land_num))

            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and map_arr[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        land_dict[(nx, ny)] = land_num
                        land_list.append((nx, ny, land_num))
            land_num += 1

edges = []

# 인접한 땅 사이의 엣지 체크
for x, y, cur_land in land_list:
    for d in range(4):
        distance = 0
        nx, ny = x + dx[d], y + dy[d]
        while True:
            if 0 <= nx < N and 0 <= ny < M:
                to_land = land_dict.get((nx, ny))
                if cur_land == to_land:
                    break
                if to_land is None:
                    nx += dx[d]
                    ny += dy[d]
                    distance += 1
                    continue
                if distance < 2:
                    break
                edges.append((distance, cur_land, to_land))
                break
            else:
                break

# 거리를 기준으로 내림차순으로 엣지를 정렬
edges = sorted(edges, reverse=True)

# Union-Find 구조
def union(x, y):
    x = find(x)
    y = find(y)
    parents[y] = x

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

# 결과와 연결된 구성 요소의 개수를 초기화
ans = 0
cnt = land_num - 1

# 유니온-파인드를 위한 부모 배열을 초기화
parents = [i for i in range(land_num)]

# 크루스칼 최소 신장 트리를 생성
while cnt:
    try:
        w, a, b = edges.pop()
    except IndexError:
        print(-1)
        sys.exit()
    if find(a) != find(b):
        union(a, b)
        ans += w
        cnt -= 1

# 모든 땅을 연결하는데 필요한 최소 비용 출력
print(ans)