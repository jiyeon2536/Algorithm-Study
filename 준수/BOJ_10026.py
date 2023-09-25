# 이차원 배열과 색상과 좌표
def dfs(matrix, color, x, y):
    for move in range(4):
        nx = x + dx[move]
        ny = y + dy[move]

        # 인접한 칸의 색상이 같은 색상이면
        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == color:
            # 흰색으로 색상을 바꾸고 그 칸에서 다시 탐색
            matrix[nx][ny] = 'W'
            dfs(matrix, color, nx, ny)


import sys
sys.setrecursionlimit(10000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

# 이차원 배열 입력
arr1 = [list(input()) for _ in range(N)]

# 'G'를 'R'로 바꾸면서 이차원 배열 복사
arr2 = []

for line in arr1:
    tmp_line = []
    
    for color in line[:]:
        if color == 'G':
            tmp_line.append('R')
        else:
            tmp_line.append(color)
    
    arr2.append(tmp_line)

arr1_cnt = 0
arr2_cnt = 0

# arr1과 arr2의 모든 칸을 순회...
# 그 칸이 흰색이 아니라면 dfs 함수 호출
for i in range(N):
    for j in range(N):
        if arr1[i][j] != 'W':
            arr1_cnt += 1
            dfs(arr1, arr1[i][j], i, j)

        if arr2[i][j] != 'W':
            arr2_cnt += 1
            dfs(arr2, arr2[i][j], i, j)

print(arr1_cnt, arr2_cnt)