import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

arrangement = [list(input().rstrip()) for _ in range(5)]

visited = [[0] * 5 for _ in range(5)]

# BFS로 일단 가능한 좌표 조합 다 집어 넣고 배열 길이 구하면 ... ?
# S가 4개 이상 존재해야하는 조건 ... (+ 중간 백트래킹)

seven_princes = deque()
result = 0
for y in range(5):
    for x in range(5):
        # 무조건 S가 포함되어야하니까...
        # S에서 시작하자
        # --- S에서 시작할 필요가 없구나 ...
        # 그냥 모든 결과를 구하고 순서 바뀐 대로 나누기 2를 하면 될까 ... ?
        if arrangement[y][x] == 'Y':
            seven_princes.append([x, y, arrangement[y][x], 1])
        else:
            seven_princes.append([x, y, arrangement[y][x], 0])
        while seven_princes:
            visited = [[0] * 5 for _ in range(5)]
            x, y, selection, cnt = seven_princes.popleft()
            visited[y][x] = 1
            if cnt >= 4:
                continue
            if len(selection) == 7:
                result += 1
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                    if arrangement[ny][nx] == 'Y':
                        seven_princes.append([nx, ny, arrangement[ny][nx], cnt + 1])
                    else:
                        seven_princes.append([nx, ny, arrangement[ny][nx], cnt])

print(result)