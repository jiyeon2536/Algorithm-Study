import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

coin = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q1 = deque([coin[0]])
    q2 = deque([coin[1]])
    q3 = deque([1])
    q = [q1, q2, q3]

    while q[0]:
        x1, y1 = q[0].popleft()
        x2, y2 = q[1].popleft()
        cnt = q[2].popleft()
        for k in range(4):
            nx1, ny1 = x1+dx[k], y1+dy[k]
            nx2, ny2 = x2+dx[k], y2+dy[k]
            # 둘 다 보드 밖에 있을 때
            if ((0 > nx2 or nx2 >= N) or (0 > ny2 or ny2 >= M)) \
                 and ((0 > nx1 or nx1 >= N) or (0 > ny1 or ny1 >= M)):
                continue
            # 둘 중 하나만 보드 밖에 있을 때
            elif ((0 <= nx1 < N and 0 <= ny1 < M) and ((0 > nx2 or nx2 >= N) or (0 > ny2 or ny2 >= M))) \
            or ((0 <= nx2 < N and 0 <= ny2 < M) and ((0 > nx1 or nx1 >= N) or (0 > ny1 or ny1 >= M))):
                checked = True
                return cnt
            # 둘 다 보드 안에 있을 때
            elif (0 <= nx1 < N and 0 <= ny1 < M) and (0 <= nx2 < N and 0 <= ny2 < M):
                # 둘 다 벽일 때
                if board[nx1][ny1] == '#' and board[nx2][ny2] == '#':
                    continue
                # coin1만 벽일 때
                elif board[nx1][ny1] == '#':
                    if (nx1, ny1) != (nx2, ny2) and cnt <= 9:
                        q[0].append((x1, y1))
                        q[1].append((nx2, ny2))
                        q[2].append(cnt+1)
                # coin2만 벽일 때
                elif board[nx2][ny2] == '#':
                    if (nx1, ny1) != (nx2, ny2) and cnt <= 9:
                        q[0].append((nx1, ny1))
                        q[1].append((x2, y2))
                        q[2].append(cnt+1)
                # 둘 다 벽이 아닐 때
                else:
                    if cnt <= 9:
                        q[0].append((nx1, ny1))
                        q[1].append((nx2, ny2))
                        q[2].append(cnt+1)
    return -1

res = bfs()
if res > 10:
    res = -1
print(res)
