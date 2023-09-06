di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
false = [[-1] * M for _ in range(N)]
shark = []
rear = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            false[i][j] = 0
            shark.append((i, j))
            rear += 1
#print(shark)
front = 0
mx = 0
while front < rear:
    x, y = shark[front]
    for k in range(8):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == 0 and false[ni][nj] == -1:
                false[ni][nj] = false[x][y] + 1
                rear += 1
                shark.append((ni, nj))
                if mx < false[ni][nj]:
                    mx = false[ni][nj]
    front += 1
print(mx)
