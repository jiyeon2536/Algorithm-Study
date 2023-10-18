import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def BFS():
    queue = deque()
    # 시작점
    queue.append((0, 0))
    cnt = [[0] * N for _ in range(N)]
    cnt[0][0] = 1
    while queue:
        x, y = queue.popleft()
        # 도착점 도달
        if x == N-1 and y == N-1:
            return cnt[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not cnt[nx][ny]:
                # 흰방인 경우
                if maze[nx][ny] == 1:
                    # 통과
                    queue.appendleft((nx, ny))
                    cnt[nx][ny] = cnt[x][y]
                # 검은방인 경우
                else:
                    # 통과 후
                    queue.append((nx, ny))
                    # 검은방 카운트
                    cnt[nx][ny] = cnt[x][y] + 1


N = int(input())
maze = []
for i in range(N):
    maze.append(list(map(int, input().strip())))

print(BFS())