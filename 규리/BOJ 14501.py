N = int(input())  # 남은 N일
T = []  # 상담 완료하는데 걸리는 기간
P = []  # 상담 했을 때 받을 수 있는 금액
for _ in range(N):
    t, p = map(int, input().split())  # 상담완료기간, 금액
    T.append(t)
    P.append(p)

DP = [0]*(N+1)

for i in range(N-1, -1, -1):
    if T[i] + i > N:  # N일만에 상담을 끝낼 수 없다면
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], P[i] + DP[i+T[i]])

print(DP[0])
