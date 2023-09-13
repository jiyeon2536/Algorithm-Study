from collections import deque
import sys
input = sys.stdin.readline

# 상자 크기 가로 M, 세로 N, 쌓아올려지는 수 H
M, N, H = map(int, input().split())
# 1:익음 / 0:익지않음 / -1:토마토없음
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# box[z][x][y] - z:층수 / x:세로 / y:가로
dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

tmt = deque()

for h in range(H):          # 층
    for n in range(N):      # 세로
        for m in range(M):  # 가로
            if box[h][n][m] == 1:
                tmt.append((h, n, m))

mx = 0
while tmt:
    z, x, y = tmt.popleft()
    for k in range(6):
        nz, nx, ny = z + dz[k], x + dx[k], y + dy[k]
        if nz in range(0, H) and nx in range(0, N) and ny in range(0, M) and box[nz][nx][ny] == 0:
            box[nz][nx][ny] = box[z][x][y] + 1
            mx = max(box[nz][nx][ny], mx)
            tmt.append((nz, nx, ny))

result = mx - 1
check = True
# 토마토가 다 익지 않은 경우
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                check = False
                break
if check == False:
    result = -1
# 토마토가 이미 다 익어있는 경우
elif check == True and mx == 0:
    result = 0

print(result)
