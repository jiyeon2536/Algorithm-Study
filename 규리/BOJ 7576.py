from collections import deque
import sys
input = sys.stdin.readline

# 상자 크기 가로 M, 세로 N
M, N = map(int, input().split())
# 1:익음 / 0:익지않음 / -1:토마토없음
box = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tmt = deque()

for n in range(N):      # 세로
    for m in range(M):  # 가로
        if box[n][m] == 1:
            tmt.append((n, m))

mx = 0
while tmt:
    x, y = tmt.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx in range(0, N) and ny in range(0, M) and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            mx = max(box[nx][ny], mx)
            tmt.append((nx, ny))

result = mx - 1
check = True
# 토마토가 다 익지 않은 경우
for n in range(N):
    for m in range(M):
        if box[n][m] == 0:
            check = False
            break
if check == False:
    result = -1
# 토마토가 이미 다 익어있는 경우
elif check == True and mx == 0:
    result = 0

print(result)
