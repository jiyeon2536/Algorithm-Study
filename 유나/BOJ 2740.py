import sys
input = sys.stdin.readline

# 행렬 a의 크기 n행 m열 / b 행렬 크기 m행 n열
n, m = map(int, input().strip().split())
a = [list(map(int, input().strip().split())) for _ in range(n)]

s, k = map(int, input().strip().split())
b = [list(map(int, input().strip().split())) for _ in range(s)]

# 결과를 받을 변수 생성 n행 k열
res = [[0] * k for _ in range(n)]

# i행 j열 값을 계산하기 위해 순회
# A의 열, B의 행만큼 순회하면 값 더해줌
for i in range(n):
    for j in range(k):
        for l in range(m):
            res[i][j] += a[i][l] * b[l][j]

for item in res:
    print(*item)
