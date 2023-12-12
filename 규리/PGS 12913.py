def solution(land):
    N = len(land)
    DP = [[0]*4 for _ in range(N)]
    DP[0] = land[0]
    
    for i in range(1, N):
        # for j in range(4):
        #     # DP[i][j] = max(DP[i-1][:j], DP[i-1][j+1:]) + land[i][j]
        #     arr = []
        #     for k in range(4):
        #         if j != k:
        #             arr.append(DP[i-1][k])
        #     DP[i][j] = max(arr) + land[i][j]
            
        DP[i][0] = max(DP[i-1][1], DP[i-1][2], DP[i-1][3]) + land[i][0]
        DP[i][1] = max(DP[i-1][0], DP[i-1][2], DP[i-1][3]) + land[i][1]
        DP[i][2] = max(DP[i-1][0], DP[i-1][1], DP[i-1][3]) + land[i][2]
        DP[i][3] = max(DP[i-1][0], DP[i-1][1], DP[i-1][2]) + land[i][3]
    
    mx = max(DP[i])
    
    return mx
