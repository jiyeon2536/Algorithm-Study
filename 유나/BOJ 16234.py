from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global cnt, total, change, work
    que = deque()
    que.append(start)
    while que:
        i, j = que.popleft()
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and l <= abs(arr[i][j] - arr[ni][nj]) <= r and visited[ni][nj] == 0:
                visited[i][j] = 1 # 여기 넣은 이유 : 값이 바뀐 적 없다면 방문할 수 있도록 하기 위해
                visited[ni][nj] = 1
                que.append((ni, nj))
                cnt += 1
                total += arr[ni][nj]
                change = True
                work.append((ni, nj))


# N, 최소 차이, 최대 차이
n, l, r = map(int, input().strip().split())

# 국가별 인구 수
arr = [list(map(int, input().strip().split())) for _ in range(n)]

# res 인구 이동 횟수
res = 0

# 전체 인덱스를 순회하면서 일자별로 인구이동 마치기
while True:
    visited = [[0] * n for _ in range(n)]
    change = False # 인구 이동이 발생했나요?
    for i in range(n):
        for j in range(n):
            #  방문한 적 없다면 bfs 진행
            if visited[i][j] == 0:
                cnt = 1 # 인구 이동 국가 수
                total = arr[i][j] # 총 인구 이동 수
                work = [(i, j)] # 인구 이동 작업을 위한 인덱스 리스트
                bfs((i, j))

                # bfs 종료 후 인구 이동 작업
                if change:
                    population = total // cnt
                    for k, s in work: # 국경선 열린 국가 인덱스
                        arr[k][s] = population

    # 인구 이동 작업이 이루어졌다면 res + 1
    if change:
        res += 1
    else: # 전체 인덱스를 돌았음에도 인구 이동이 이루어지지 않았다면
        break

print(res)
