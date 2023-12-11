def solution(land):
    mx = 0
    # dp인건 알겠음
    visited = [[0] * 4 for _ in range(len(land))]
    for i in range(1, len(land)):
        for j in range(4):
            if j == 0:
                land[i][j] = land[i][j] + max(land[i-1][3], land[i-1][1], land[i-1][2])
            elif j == 1:
                land[i][j] = land[i][j] + max(land[i-1][0], land[i-1][3], land[i-1][2])
            elif j == 2:
                land[i][j] = land[i][j] + max(land[i-1][0], land[i-1][1], land[i-1][3])
            elif j == 3:
                land[i][j] = land[i][j] + max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[len(land)-1])
