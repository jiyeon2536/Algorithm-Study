# 경로단축 find
def find(elem):
	if island[elem] == elem:
		return elem

	island[elem] = find(island[elem])
	return island[elem]


# union
def union(x, y):
	x = find(x)
	y = find(y)

	if x > y:
		island[x] = y
	else:
		island[y] = x


# 섬과 섬을 이을 수 있는 다리를 찾는다 
def check_bridge(x, y, num):
	# 4방향으로 한 칸을 전진해본다
	for move in range(4):
		go = 1

		while True:
			nx = x + dx[move] * go
			ny = y + dy[move] * go

            # 섬의 경계 검사
			if 0 <= nx < N and 0 <= ny < M:
				# 다음 칸이 바다라면 한 칸 더 전진
				if country[nx][ny] == 0:
					go += 1
				# 다음 칸이 시작한 섬의 칸이 아니면서 다리의 길이가 2 이상일 경우
				elif country[nx][ny] != num and go > 2:
					# 다리의 길이, 시작 섬의 번호, 도착 섬의 번호를 우선순위 큐에 저장
					heapq.heappush(bridge_list, (go - 1, num, country[nx][ny]))
					break
				else:
					break
			else:
				break


# 인접한 모든 칸을 탐색하며 섬인 부분을 같은 번호로 통일 
def check_island(sx, sy, num):
	queue = deque([(sx, sy)])

	while queue:
		x, y = queue.popleft()

		for move in range(4):
			nx = x + dx[move]
			ny = y + dy[move]

			if 0 <= nx < N and 0 <= ny < M and country[nx][ny] == 1:
				country[nx][ny] = num
				queue.append((nx, ny))


import heapq
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
# 배열에 1이 있으므로 2부터 시작
island_num = 2

for i in range(N):
	for j in range(M):
		if country[i][j] == 1:
			country[i][j] = island_num
			check_island(i, j, island_num)
			# 다음 섬을 위해 번호를 갱신
			island_num += 1

# 지을 수 있는 다리의 후보를 담는 큐
bridge_list = []

# 섬의 집합을 표현한 배열
island = [_ for _ in range(island_num)]

for i in range(N):
	for j in range(M):
		if country[i][j]:
			check_bridge(i, j, country[i][j])

# 최소 비용으로 연결된 다리의 총 비용
total_cost = 0
# 연결된 다리의 개수
connect_num = 0

while bridge_list:
	cost, start, end = heapq.heappop(bridge_list)
	
    # 여기에 visited 추가한다면 더 시간 단축이 될 듯...

    # 연결되어있지 않은 섬이면 연결하면서 최소 비용을 총 비용에 더함
	if find(start) != find(end):
		connect_num += 1
		total_cost += cost
		union(start, end)

# 연결된 다리의 개수와 (섬의 개수 - 1)가 다르면 -1
if island_num > connect_num + 3:
	print(-1)
else:
	print(total_cost)