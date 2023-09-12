import sys
input = sys.stdin.readline

# A 행렬의 크기와 요소
NA, MA = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(NA)]
# B 행렬의 크기와 요소
NB, MB = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(NB)]

# 결과는 NA * MB 행렬이 되므로 다음과 같이 arr 범위설정
arr = [[0 for _ in range(MB)] for _ in range(NA)]

# NA * MB 행렬 내에서 MA 의 NB 크기가 같다
# A 행렬에서 MA 가 행을 순회하고 B 행렬에서 MA 가 열을 순회하므로
for i in range(NA):
    for j in range(MB):
        for k in range(MA):
            arr[i][j] += matrixA[i][k] * matrixB[k][j]

for u in arr:
    print(*u)
