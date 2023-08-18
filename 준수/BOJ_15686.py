# depth의 개수만큼만 치킨 가게를 남기고 폐업시키는 함수
def dfs(depth, arr, closed):
    # 앞 단계의 closed 리스트를 받아서 새롭게 선언
    new_closed = closed[:]

    # 고른 치킨 가게의 수가 depth일 경우...
    if depth == M:
        return bfs(arr)

    # 현재 치킨 가게 중 몇 개만 고른다
    for v in range(len(chicken)):
        if new_closed[v] == False:
            new_closed[v] = True
            dfs(depth + 1, arr + [chicken[v]], new_closed)
            # new_closed[v] = False
            # 위의 코드를 적지 않는 이유 => 중복을 허용하지 않기 때문
            # ex) [[0, 1], [2, 3]]과 [[2, 3], [0, 1]] 중 하나만 필요


def bfs(arr):
    global mn

    visited = [[False] * N for _ in range(N)]
    queue = deque(arr)
    distance = 0

    new_city = []

    for n in city:
        tmp_line = []
        for m in n:
            if m == 2:
                tmp_line.append(0)
            else:
                tmp_line.append(m)
        new_city.append(tmp_line)

    while queue:
        # 치킨 가게에서 1칸씩 멀어지면 distance가 1씩 증가
        distance += 1
        # queue에 담긴 각 경우의 수를 일단 모두 순회하는 for문
        for _ in range(len(queue)):
            coord = queue.popleft()
            x = coord[0]
            y = coord[1]
            visited[x][y] = True

            # 상하좌우 델타탐색
            for move in range(4):
                nx = x + dx[move]
                ny = y + dy[move]

                # 범위 및 방문 여부 체크
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                    # 집을 발견한 경우... 치킨 가게와의 거리를 기록
                    # visited에 의해 최소 거리만 기록됨
                    if new_city[nx][ny] == 1:
                        new_city[nx][ny] = distance

    res = 0

    # 치킨 가게와 집들의 사이의 최소 거리들을 모두 더함
    for r in range(N):
        for c in range(N):
            if new_city[r][c]:
                res += new_city[r][c]

    # 폐업 후 남은 치킨 가게의 모든 경우의 수에 대해 최소값을 구함 
    if mn > res:
        mn = res


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

city = []
chicken = deque()

# 시작점의 좌표를 찾고 도시를 이차원 리스트로 만듦
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            chicken.append([i, j])
    city.append(line)

# 폐업시켜야 할 치킨 가게 목록 초기화 
closed_chicken = [False] * len(chicken)

# 내 생일
mn = 980309
dfs(0, [], closed_chicken)

print(mn)