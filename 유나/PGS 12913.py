def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # 이전 행에서 자기 자신의 자리(인덱스)를 제외한 최댓값을 더함
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land)-1])
