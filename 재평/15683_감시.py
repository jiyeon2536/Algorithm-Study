import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for y in range(N):
    for x in range(M):
        if 1 <= arr[y][x] <= 5:
            cctv.append((x, y, arr[y][x]))

def dfs(idx, arr):
    global ans
    if idx == len(cctv):
        cnt = 0
        for y in range(N):
            for x in range(M):
                if arr[y][x] == 0:
                    cnt += 1
        ans = min(ans, cnt)
        return
    x, y, num = cctv[idx]
    if num == 1:
        for i in range(4):
            tmp = [[arr[y][x] for x in range(M)] for y in range(N)]
            for j in range(1, 8):
                nx, ny = x + j*dx[i], y + j*dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            dfs(idx+1, tmp)
    elif num == 2:
        for i in range(2):
            tmp = [[arr[y][x] for x in range(M)] for y in range(N)]
            for j in range(1, 8):
                nx, ny = x + j*dx[i], y + j*dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            for j in range(1, 8):
                nx, ny = x + j*dx[i+2], y + j*dy[i+2]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            dfs(idx+1, tmp)
    elif num == 3:
        for i in range(4):
            tmp = [[arr[y][x] for x in range(M)] for y in range(N)]
            for j in range(1, 8):
                nx, ny = x + j*dx[i], y + j*dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            for j in range(1, 8):
                nx, ny = x + j*dx[(i+1)%4], y + j*dy[(i+1)%4]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            dfs(idx+1, tmp)
    elif num == 4:
        for i in range(4):
            tmp = [[arr[y][x] for x in range(M)] for y in range(N)]
            for j in range(1, 8):
                nx, ny = x + j*dx[i], y + j*dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            for j in range(1, 8):
                nx, ny = x + j*dx[(i+1)%4], y + j*dy[(i+1)%4]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            for j in range(1, 8):
                nx, ny = x + j*dx[(i+2)%4], y + j*dy[(i+2)%4]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
            dfs(idx+1, tmp)
    elif num == 5:
        tmp = [[arr[y][x] for x in range(M)] for y in range(N)]
        for i in range(4):
            for j in range(1, 8):
                nx, ny = x + j*dx[i], y + j*dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if tmp[ny][nx] == 6:
                        break
                    elif tmp[ny][nx] == 0:
                        tmp[ny][nx] = -1
        dfs(idx+1, tmp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 64
dfs(0, arr)
print(ans)