def bfs(sx, sy):
	queue = deque([(sx, sy)])
	population = countries[sx][sy]
	unity = [(sx, sy)]
	visited[sx][sy] = True

	while queue:
		x, y = queue.popleft()

		for move in range(4):
			nx = x + dx[move]
			ny = y + dy[move]

			if 0 <= nx < N and 0 <= ny < N:
				diff = abs(countries[x][y] - countries[nx][ny])

				if L <= diff <= R and not visited[nx][ny]:
					unity.append((nx, ny))
					population += countries[nx][ny]
					visited[nx][ny] = True
					queue.append((nx, ny))

	average = population // len(unity)

	for x, y in unity:
		countries[x][y] = average

	if len(unity) >= 2 or is_unity:
		return True
	else:
		return False


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

days = 0

while True:
	visited = [[False] * N for _ in range(N)]
	is_unity = False

	for i in range(N):
		for j in range(N):
			if not visited[i][j]:
				is_unity = bfs(i, j)

	if is_unity:
		days += 1
	else:
		break

print(days)