from collections import deque
import sys
input = sys.stdin.readline

# nxn
n = int(input().strip())

# map
arr = [list(map(int, input().strip().split())) for _ in range(n)]

def bfs(i, j):
    global size, cnt, total, si, sj
    que = deque()
    que.append((i, j))
    visited = [[0] * n for _ in range(n)]
    check = 0 # 먹이 잡았는지 체크
    eat = []
    while que:
        i, j = que.popleft()
        # 가장 높 > 가장 왼 : 상 좌 우 하
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            ni, nj = i + di, j + dj
            # 범위 내에 존재하고, 물고기의 크기가 상어보다 작거나 같고, 방문한 적이 업다면
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] <= size and visited[ni][nj] == 0:
                # 물고기가 없거나, 사이즈가 동일한 경우
                # 방문 체크 후 que에 append
                if arr[ni][nj] == 0 or arr[ni][nj] == size:
                    visited[ni][nj] = visited[i][j] + 1
                    # 먹을 수 있는 물고기 찾기 전인 경우에만
                    if check == 0:
                        que.append((ni,nj))
                # 상어보다 작은 물고기 존재 시!!!
                # cnt + 1
                # cnt == size : size + 1, 물고기 먹은 수 초기화
                # 딕셔너리에서 물고기 수 줄이기
                # 상어 위치 변경
                else:
                    # 방문 체크
                    visited[ni][nj] = visited[i][j] + 1
                    # 걸린 시간, x좌표, y좌표 추가
                    eat.append((visited[ni][nj], ni, nj))

    if eat:
        eat.sort(key = lambda x: [x[0], x[1], x[2]])
        return eat[0]
    return
# 체크 하면 거리, x, y축 어펜드 안하게 그 거리에서 먹을 수 있는거?
# que 거리에 있는 애 들까지만 돌면서

# 초기 아기상어의 위치 si, sj
si = sj = 0
for i in range(n):
    for j in range(n):
        # 아기 상어 위치 체크, 0으로 초기화
        if arr[i][j] == 9:
            arr[i][j] = 0
            si, sj = i, j

# 아기상어의 초기 크기
size = 2
# 먹은 물고기의 수
cnt = 0
# 최종 걸린 시간 total
total = 0

while True:
    res = bfs(si, sj)
    if res:
        times, ti, tj = res
        arr[ti][tj] = 0
        cnt += 1
        total += times
        si, sj = ti, tj
        if size == cnt:
            size += 1
            cnt = 0
    else:
        break
