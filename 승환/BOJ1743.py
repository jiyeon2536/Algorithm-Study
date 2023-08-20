import sys
sys.setrecursionlimit(10**7)
def findbfs(x, y):
    global cnt
    q.append((x, y))
    while q:
        x, y = q.pop(0)
        arr[x][y] = 0
        cnt += 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                q.append((nx, ny))


N, M, K = map(int, input().split())  # N = 세로길이, M = 가로길이, K = 음식물 쓰래기 수
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
q = []
mx = 0
for x in range(N):
    for y in range(M):
        cnt = 0
        if arr[x][y] == 1:
            findbfs(x, y)
            mx = max(mx, cnt)
print(mx)
# 시간초과 난 BFS 코드
# 아래 DFS? 코드는 통과함
def findt(x, y):
    arr[x][y] = 0  # 확인한 쓰레기는 다시 확인하지 않는다.
    global cnt
    cnt += 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
            findt(nx, ny)


N, M, K = map(int, input().split())  # N = 세로길이, M = 가로길이, K = 음식물 쓰래기 수
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

res = 0
for x in range(N):
    for y in range(M):
        cnt = 0
        if arr[x][y] == 1:
            findt(x, y)
            res = max(res, cnt)
print(res)

'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''
