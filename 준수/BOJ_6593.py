# 상범아 탈출하자...!
def bfs(start, end):
    queue = deque([start])
    ez, ex, ey = end
    time = 0

    while queue:
        # 1초가 흐를 때마다 상범이가 위치할 수 있는 경우의 수
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            
            # 탈출!
            if z == ez and x == ex and y == ey:
                print(f'Escaped in {time} minute(s).')
                return

            for move in range(6):
                nz = z + dz[move]
                nx = x + dx[move]
                ny = y + dy[move]

                # 왔던 길은 '#'로 바꾸어 더 이상 가지 못하게 함!
                if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                    if building[nz][nx][ny] == '.':
                        building[nz][nx][ny] = '#'
                        queue.append([nz, nx, ny])

        # 1초가 흐름
        time += 1

    # 탈출을 못 했을 경우...
    print('Trapped!')


import sys
input = sys.stdin.readline
from collections import deque

# 층(z축), 세로(x축), 가로(y축)
dz = [1, 0, 0, -1, 0, 0]
dx = [0, 1, 0, 0, -1, 0]
dy = [0, 0, 1, 0, 0, -1]

while True:
    L, R, C = map(int, input().split())

    # 입력이 끝나는 시점
    if L == R == C == 0:
        break

    # 빌딩 짓기 시작!
    building = []

    # 층, 세로, 가로
    sz, sx, sy = -1, -1, -1
    ez, ex, ey = -1, -1, -1

    for l in range(L):
        plane = []

        for r in range(R):
            line = list(input())

            # 한 줄 한 줄 검사해보기
            for c in range(C):
                if line[c] == 'S':
                    line[c] = '#'
                    sz, sx, sy = l, r, c

                if line[c] == 'E':
                    line[c] = '.'
                    ez, ex, ey = l, r, c

            # 한 층씩 만드는 중!
            plane.append(line)

        # 빌딩을 한 층씩 쌓습니다...!
        building.append(plane)
        # 쓸모없는 공백 제거
        blank = input()

    bfs([sz, sx, sy], [ez, ex, ey])