import sys
input = sys.stdin.readline
from collections import deque

# 사방탐색
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def BFS(x, y):
    migration = deque()
    result = []
    migration.append((x, y))
    result.append((x, y))
    while migration:
        x, y = migration.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if L <= abs(continent[ny][nx] - continent[y][x]) <= R:
                    visited[ny][nx] = True
                    migration.append((nx, ny))
                    result.append((nx, ny))
    return result

N, L, R = map(int, input().split())
continent = []
for _ in range(N):
    continent.append(list(map(int,input().split())))

result = 0
while True:
    visited = [[False] * N for _ in range(N)]
    check = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                visited[y][x] = True
                # 연결된 국가
                union = BFS(x, y)
                cnt = len(union)
                if cnt > 1:
                    check = 1
                    # 평균 인구
                    population = 0
                    for x, y in union:
                        population += continent[y][x]
                    population //= cnt
                    for x, y in union:
                        continent[y][x] = population
    if check == 0:
        break
    result += 1
print(result)