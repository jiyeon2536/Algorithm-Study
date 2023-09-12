N, M = map(int, input().split())

A_list = []
B_list = []

# A 행렬을 만듦 
for _ in range(N):
    A = list(map(int, input().split()))
    A_list.append(A)

M, K = map(int, input().split())

# B 행렬을 만듦
for _ in range(M):
    B = list(map(int, input().split()))
    B_list.append(B)

# 행렬 곱셈의 결과를 담는 이차원 배열
dp = [[0 for _ in range(K)] for _ in range(N)]

# 행렬 곱셈 -> 아직도 어떻게 하는지 모름
# 그냥 인터넷에서 행렬은 이렇게 연산하래
for i in range(N):
    for k in range(K):
        tmp_sum = 0
        for j in range(M):
            tmp_sum += A_list[i][j] * B_list[j][k]
        dp[i][k] = tmp_sum

for output in dp:
    print(*output)