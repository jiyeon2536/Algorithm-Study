from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr):
    visited = [[[0] * m for _ in range(n)] for _ in range(2)]# 얘는 2차원 배열
    que = deque()
    # 상태, 행, 열
    que.append((0,0,0))
    visited[0][0][0] = 1
    while que:
        check, i, j = que.popleft()

        # 목표 지점에 도착한다면 return
        if i == n-1 and j == m-1:
            # pprint(visited)

            return visited[check][i][j]

        for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
            ni, nj = i + di, j + dj
            # 다음 행선지가 범위내에 존재한다면
            if 0 <= ni < n and 0 <= nj < m:
                # 현재 위치로 이동할 수 있고, 아직 방문한 적 없다면
                if arr[ni][nj] == 0 and visited[check][ni][nj] == 0:
                    visited[check][ni][nj] = visited[check][i][j] + 1
                    que.append((check, ni, nj))
                # 현재 위치가 벽이고, 아직 벽을 부순 적이 없다면
                elif arr[ni][nj] == 1 and check == 0:
                    visited[1][ni][nj] = visited[check][i][j] + 1
                    que.append((1, ni, nj))
    return -1

n, m = map(int, input().strip().split())

# 벽을 부수기 전 세계
arr = [list(map(int, input().strip())) for _ in range(n)]

# 벽 하나씩 부수고 이동하기
answer = bfs(arr)
print(answer)
